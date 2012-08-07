from commProd.models import *

import random

"""
To test:
python manage.py shell
from helpers.commprod_search import commprod_search

unvoted: passing in username and receive commprods unvoted by user
"""
def commprod_search(page=0, cp_id=None, query=None, orderBy='date', direction='hl', username=None, startDate=None, endDate=None, limit=None, unvoted=False, media=False):
  commprods = CommProd.objects.all()
  print media
  try:
    if cp_id:
      commprods = commprods.filter(id=cp_id)

    if username:
      commprods = commprods.filter(user_profile__user__username=username)

    if query:
      commprods = commprods.filter(content__contains=query)

    if orderBy:
      if direction == 'lh':
        orderBy = '-' + orderBy

      commprods = commprods.order_by(orderBy, 'date')

    if startDate:
      commprods = commprods.objects.filter(date__gte=startDate)

    if endDate:
      commprods = commprods.objects.filter(date__lte=endDate)

    if unvoted:
      commprods = commprods.exclude(rating__user_profile__user__username=unvoted)
    
    if media:
      commprods = commprods.objects.filter(media=True) #exclude False is faster?

      # if random.random() > .5:
      #   commprods_exclude = commprods.exclude(score=0)
      #   if commprods_exclude.exists():
      #     commprods = commprods_exclude

    if limit:
      commprods = commprods[:limit]

  except:
    commprods = CommProd.objects.all()

  return commprods.select_related()


