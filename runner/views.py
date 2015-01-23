from datetime import datetime
from collections import Counter
from itertools import imap
from traceback import print_tb
import json

from annoying.decorators import ajax_request

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import utc
from django.db.models import Count
from django.conf import settings
from django.core import serializers
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

from runner.models import Category, Drink, RunItem, Run


# Populate the page with "my drinks" and "all drinks"
@ensure_csrf_cookie
@login_required
def index(request, run_id=None, sortby='name'):
    runs = Run.objects.all()
    if not runs:
        # If there are no runs in the database, create one
        run = Run()
        run.name = "Test Run"
        run.save()
    elif not run_id:
        run = runs.reverse()[0]
    else:
        run = Run.objects.get(pk=run_id)

    context = {
        'run': _json_run(run),
        'all_drinks': _json_drinks(),
        'categories': _json_categories(),
        'my_drinks': _get_user_order(request.user, run),
        'page_title': 'Burton Third\'s premier beverage delivery service',
        'nav_runner': 'active'
    }
    context.update(csrf(request))
    return render(request, 'runner/index.html', context)


# Get all categories and drinks as JSON
@login_required
def get_all_drinks(request):
    cat_dat = json.loads(serializers.serialize('json', Category.objects.all()))
    drink_dat = json.loads(serializers.serialize('json', Drink.objects.all()))
    all = json.dumps({'categories': cat_dat, 'drinks': drink_dat})
    return HttpResponse(all, mimetype='application/json')


# Get all items the user has for the requested run, as JSON
@login_required
def get_order(request, run_id):
    return HttpResponse(_get_user_order(request.user,
        run=Run.objects.get(pk=run_id)), mimetype='application/json')


# Called by AJAX when a user submits his/her items to the order
# the data will be in the form {drink_id: count}
@login_required
def update_run(request, run_id):
    run = Run.objects.get(pk=run_id)
    for drink_id, count in map(lambda (d, c): (int(d), int(c)), request.POST.items()):
        drink = Drink.objects.get(pk=drink_id)
        my_items = RunItem.objects.filter(
                drink__id=drink_id, customer=request.user, run=run).count()
        delta = count - my_items
        now = datetime.utcnow().replace(tzinfo=utc)

        # If there are more items in the ajax call than the DB, we add some
        if delta > 0:
            for i in range(delta):
                item = RunItem(
                        drink=drink,
                        customer=request.user,
                        run=run,
                        time=now)
                item.save()
        # if there are fewer, delete some
        elif delta < 0:
            for i in range(-delta):
                RunItem.objects.filter(
                        customer=request.user,
                        run=run,
                        drink=drink)[0].delete()

    # if the run has reached a threshold order size, give it an end date and
    # notify the run master
    if run.total_price() >= run.goal:
        # is it too late for the run to go out today?
        if datetime.datetime.now().hour >= 17:
            run.end_date = datetime.datetime.tomorrow(12) # tomorrow at 12 pm
        else:
            run.end_date = datetime.datetime.now + 1 # in one hour
        email_runmaster(run)

    # return the updated run summary
    return HttpResponse(_json_run(run), mimetype='application/json')


# The run has reached its goal threshold: get the run master off his ass
def email_runmaster(run):
    body = _summarize_run(run)
    #do_the_thing()


# Get a list of all categories in clean json
def _json_categories():
    data = json.loads(serializers.serialize('json', Category.objects.all()))
    for d in data:
        for f, val in d['fields'].iteritems():
            d[f] = val
        del d['fields']
    return json.dumps(data)


# Get a list of all drinks in clean json
def _json_drinks():
    data = json.loads(serializers.serialize('json', Drink.objects.all()))
    for d in data:
        for f, val in d['fields'].iteritems():
            d[f] = val
        del d['fields']

        drink = Drink.objects.get(id=d['pk'])
        d['clean_volume'] = drink.clean_volume()
        d['clean_price'] = drink.clean_price()
    return json.dumps(data)


# Convert a run object to a JSO
def _json_run(run):
    total = sum([float(i.drink.price) for i in RunItem.objects.filter(run=run.id)])
    data = { 'pk': int(run.pk),
             'name': str(run.name),
             'goal': float(run.goal),
             'total': total }
    return json.dumps(data)


# Get all drinks queued for the requested order by the current user
def _get_user_order(user, run):
    my_items = RunItem.objects.filter(customer=user, run=run.id)
    my_drinks = []
    for drink in set(i.drink for i in my_items):
        # get the number of each drink the user has in his current order
        drink.count = len([i for i in my_items if i.drink == drink])
        # the page will need the icon for rendering
        my_drinks.append(drink)

    data = json.dumps({d.id: d.count for d in my_drinks})

    return data


# Summarize the order for the run master
def _summarize_run(run):
    all_items = RunItem.objects.filter(drink=drink.id, run=run.id)
    all_drinks = set(i.drink for i in all_items)
    all_users = set(i.customer for i in all_items)

    item_summaries = []
    for drink in all_drinks:
        item_summaries.append(str(len(
            [i for i in all_items if i.drink == drink]
            )) + ' ' + str(drink))

    user_summaries = []
    for u in all_users:
        my_items = [i for i in items if i.customer == u]
        my_drinks = set(i.drink for i in my_items)
        my_total = sum(i.price for i in my_items)
        summary = str(user) + ' ($' + str(my_total) + '): '
        summary += ', '.join([str(drink) +
            str(len([i for i in my_items if i.drink == drink]))
            for drink in my_drinks])
        user_summaries.append(summary)

    total = str(run.total_price())
    items = '\n'.join(item_summaries)
    user_items = '\n'.join(user_summaries)
    return run.name + '\nTotal: ' + total + '\n\n' +\
            items + '\n\n' + user_items

