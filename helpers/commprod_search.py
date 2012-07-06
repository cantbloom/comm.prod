from commProd.models import CommProd, Rating, UserProfile

"""
To test:
python manage.py shell
from helpers.commprod_search import commprod_search
"""
def commprod_search(page=0, cp_id=None, query=None, orderBy='date', direction='hl', username=None, startDate=None, endDate=None):
	commprods = CommProd.objects.all()

	try:
		if cp_id:
			commprods = commprods.filter(id=cp_id)

		if username:
			commprods = commprods.filter(user_profile__user__username=username)

		if query:
			commprods = commprods.filter(commprod_content__contains=query)

		if orderBy:
			if direction == 'lh':
				orderBy = '-' + orderBy
			elif direction == 'hl': 
				commprods = commprods.order_by(orderBy)

		if startDate:
			commprods = commprods.objects.filter(date__gte=startDate)

		if endDate:
			commprods = commprods.objects.filter(date__lte=endDate)
	
	except:
		commprods = CommProd.objects.all()

	return commprods.select_related()


