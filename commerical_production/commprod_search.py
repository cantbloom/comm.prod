from commProd.models import CommProd, Rating, UserProfile

def commprod_search(cp_id=None, query=None, orderBy='date', direction='hl', username=None, startDate=None, endDate=None ):
		commprods = CommProd.objects.all()

		if cp_id:
			commprods.filter(id=cp_id)

		if query:
			commprods.filter(content__contains=query)

		if orderBy:
			#django defaults to high to low, so just andle low to high option 
			if direction == 'lh':
				orderBy = '-' + orderBy
			commprods.orderBy(orderBy)

		if username:
			commprods.filter(username=username)

		if startDate:
			commprods.objects.filter(date__gte=startDate)

		if endDate:
			commprods.objects.filter(date__lte=endDate)
