from commProd.models import CommProd, Rating, UserProfile

#to test from commerical_production.commprod_search import commprod_search
def commprod_search(cp_id=None, query=None, orderBy='date', direction='hl', username=None, startDate=None, endDate=None ):
	commprods = CommProd.objects.all()

	if cp_id:
		commprods = commprods.filter(id=cp_id)

	if username:
		commprods = commprods.filter(user__username=username)

	if query:
		commprods = commprods.filter(content__contains=query)

	if orderBy:
		#django defaults to high to low, so just andle low to high option 
		if direction == 'lh':
			orderBy = '-' + orderBy
		commprods = commprods.order_by(orderBy)

	if startDate:
		commprods = commprods.objects.filter(date__gte=startDate)

	if endDate:
		commprods = commprods.objects.filter(date__lte=endDate)

	return commprods

