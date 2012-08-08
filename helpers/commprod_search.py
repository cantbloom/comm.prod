from commProd.models import *

import random

"""
To test:
python manage.py shell
from helpers.commprod_search import commprod_search

rec: passing in username and receive commprods in ordered by recommentdation for user
unvoted: passing in username and receive commprods unvoted by user
"""
def commprod_search(page=0, cp_id=None, query=None, orderBy='date', direction='hl', username=None, startDate=None, endDate=None, limit=None, unvoted=False, rec=False):
  commprods = None

  if rec:
      rec_object = CommProdRec.objects.filter(user_profile__user__username=rec)
      if rec_object.exists():
        commprods = rec_object[0].get_prods()

  if not commprods:
    commprods = CommProd.objects.all()

  try:

    #must be first for rec to work


    if cp_id:
      commprods = commprods.filter(id=cp_id)

    if username:
      commprods = commprods.filter(user_profile__user__username=username)

    if query:
      commprods = commprods.filter(content__contains=query)

    if orderBy and not rec:
      if direction == 'lh':
        orderBy = '-' + orderBy

      commprods = commprods.order_by(orderBy, 'date')

    if startDate:
      commprods = commprods.objects.filter(date__gte=startDate)

    if endDate:
      commprods = commprods.objects.filter(date__lte=endDate)

    if unvoted:
      commprods = commprods.exclude(rating__user_profile__user__username=unvoted)
      # if random.random() > .5:
      #   commprods_exclude = commprods.exclude(score=0)
      #   if commprods_exclude.exists():
      #     commprods = commprods_exclude

    if limit:
      commprods = commprods[:limit]
      
  except:
    commprods = CommProd.objects.all()

  return commprods


