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

    if not request.user.is_authenticated():
        request.user = authenticate(username='bcyphers', password='elixir')

    context = { 'run': _json_run(run),
                'all_drinks': _json_drinks(),
                'categories': _json_categories(),
                'my_drinks': _get_user_order(request.user, run) }
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

    # return the updated run summary
    return HttpResponse(_json_run(run), mimetype='application/json')


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


# Get the current run as a JSO
def _json_run(run):
    total = sum([float(i.drink.price) for i in RunItem.objects.filter(run=run.id)])
    data = { 'pk': int(run.pk),
             'name': str(run.name),
             'goal': float(run.goal),
             'total': total }
    return json.dumps(data)


# Get all drinks queued for the requested order by the current user.
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
