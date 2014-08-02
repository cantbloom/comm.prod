from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

from annoying.decorators import ajax_request
from annoying.decorators import render_to

import commProd.models as cpm

from helpers.admin.utils import create_user
from helpers.urlize_tags import commprod_contains_media
from helpers.view_helpers import fav_commprod
from helpers.view_helpers import vote_commprod
from helpers.view_helpers import vote_correction
from helpers.query_managers import commprod_query_manager
from helpers.query_managers import correction_query_manager
from helpers.query_managers import trend_data_manager
from helpers.query_managers import vs_data_manager
from helpers.link_activator import get_active_page
from helpers.urlize_email_content import urlize_email_content
from helpers.urlize_tags import urlize_text

from os import environ as env


@login_required
@render_to('commprod/home.html')
def home(request):
  """
      Landing page, top ten rated comm prods + ten newest commprods
  """
  profiles = cpm.UserProfile.objects.order_by('score')

  return {
      'page_title': 'Vote on these comm.prods we think you\'ll like',
      'nav_commprod': 'active',
      'subnav_home': 'active',
      # 'unvoted_commprods': str(commprod_query_manager(
      # {'unvoted':True, 'orderBy': '?', 'limit':30}, request.user, 'list')),
      'user_profile': request.user.profile,
      'num_commprods': cpm.CommProd.objects.all().count(),
      'num_votes': cpm.Rating.objects.all().count(),
      'worst_user': profiles[0],
      'best_user': profiles[len(profiles) - 1],
      'stats': 'True'

  }


@login_required
@render_to('commprod/search.html')
def search(request):
  subnav_key, subnav_value, title = get_active_page(
      'home',
      request.GET.get('type', ''))
  return {
      'page_title': subnav_key.split('_')[1],
      'nav_commprod': 'active',
      'user': request.user,
      'commprod_timeline': commprod_query_manager(
          request.GET, request.user),
      subnav_key: subnav_value
  }


@login_required
@render_to('commprod/permalink.html')
def permalink(request, username, cp_id):
  get_dict = {'username': username, 'cp_id': cp_id}

  commprod = commprod_query_manager(get_dict,
                                    request.user, return_type='list')
  if len(commprod) == 1:
    rendered_commprod = commprod[0]
    commprod = cpm.CommProd.objects.filter(id=cp_id)[0]
    corrections = correction_query_manager(
        user=request.user, commprod=commprod)

    commprods = cpm.CommProd.objects.filter(
        email_content=commprod.email_content)
    email_content = urlize_email_content(
        commprod.email_content.content, commprods)
  else:
    raise Http404

  return {
      'user': request.user,
      'page_title': 'permalink',
      'nav_commprod': 'active',
      'rendered_commprod': rendered_commprod,
      'commprod': commprod,
      'corrections': corrections,
      'email_content': email_content,
  }


@staff_member_required
@render_to('commprod/admin.html')
def admin(request):
  """
      Frontend endpoint for adding commprods
      that are not picked up by the parser
  """
  return {
      'key': env['SECRET_KEY']
  }

# ##### request endpoints #######


@login_required
@ajax_request
def end_tour(request):
  user_profile = request.user.profile
  user_profile.use_tour = False
  user_profile.save()
  return dict(res='Success!')


@login_required
@ajax_request
def vote(request):
  types = ['commprod', 'correction']
  valid_votes = ['-1', '1']  # patlsotw
  payload = {'success': False}

  score = request.POST.get('score', None)
  id = request.POST.get('id', None)
  type = request.POST.get('type', None)
  user = request.user

  if type in types and score and id:
    if type == 'commprod':
      rating, obj = vote_commprod(id, score, user)
    elif type == 'correction':
      rating, obj = vote_correction(id, score, user)

    if rating and score in valid_votes:
      rating.score = score
      rating.save()  # updates object avg automatically during save

      payload = {
          'success': True,
          'id': id,
          'rating': float(score),
          'score': obj.score,
          'type': type
      }

  return payload


@login_required
@ajax_request
def favorite(request):
  payload = {'success': False}
  id = request.POST.get('id', None)
  # convert string to boolean
  choice = json.loads(request.POST.get('choice', None))
  user = request.user
  if id and choice is not None:
    fav = fav_commprod(id, user)
    if fav:
      fav.fav = choice
      fav.save()
      payload = {
          'success': True,
          'id': id,
          'fav': choice,
      }

  return payload


@login_required
@ajax_request
def api_search(request):
  return_type = request.GET.get('return_type', 'html')
  return {
      'res': commprod_query_manager(
          request.GET, request.user, return_type)
  }


@login_required
@ajax_request
def profile_data(request):
  response_data = None  # patlsotw

  type = request.GET.get('type', None)
  filter = request.GET.get('filter', None)
  username = request.GET.get('username', None)
  if username and User.objects.filter(
          username=username).exists():
    user = User.objects.filter(username=username)[0]

    if type == 'trend':
      response_data = trend_data_manager(user)
    elif type == 'vs_data':
      response_data = vs_data_manager(user, filter)

  return response_data


@login_required
@ajax_request
def correction(request):
  user = request.user
  cp_id = request.POST.get('cp_id', None)
  content = request.POST.get('content', None)
  if cp_id and content and cpm.CommProd.objects.filter(
          id=cp_id).exists():
    commprod = cpm.CommProd.objects.filter(id=cp_id)[0]
    correction = cpm.Correction(user_profile=user.profile,
                                content=content, commprod=commprod)
    correction.save()
    response_data = {
        'correction': correction_query_manager(
            user=request.user, correction_id=correction.id)
    }
  else:
    response_data = {
        'nodata': ''
    }

  return response_data


@csrf_exempt
@ajax_request
def processProd(request):
  data = request.POST.get('data', None)
  key = request.POST.get('key', None)
  resp = ''
  if data and str(key) == env['SECRET_KEY']:
    # {sender : (content, [comm_prods], date, subject)}
    data = json.loads(data)
    sender = data.keys()[0]
    content, commprods, date, subject = data[sender]

    user = None
    email_search = User.objects.filter(email=sender)
    alt_email_search = cpm.UserProfile.objects.filter(
        email__email=sender, email__confirmed=True)

    if email_search.exists():
      user = email_search[0]
    elif alt_email_search.exists():
      user = alt_email_search[0].user
    else:
      user, created = create_user(sender, sender)

    resp += """\nUser %(sender)s with
        comm prods:\n %(commprods)s""" % {
        'sender': sender,
        'commprods': commprods
    }

    for commprod in commprods:
      email_content, created = cpm.CommProdEmail\
          .objects.get_or_create(
              user_profile=user.profile, content=content,
              subject=subject, date=date)
      if created:
        email_content.save()

      media = commprod_contains_media(commprod)
      media_content = ''
      if media:
        media_content = urlize_text(commprod)
      commprod, created = cpm.CommProd.objects.get_or_create(
          email_content=email_content,
          content=commprod,
          original_content=commprod,
          user_profile=user.profile,
          media=media,
          media_content=media_content,
          date=date)
      if created:
        commprod.save()
      resp += '\nAdded? %s' % created
  else:
    resp = 'No data'
    if str(key) != env['SECRET_KEY']:  # patlsotw
      resp = 'Success!'
  return dict(res=resp)
