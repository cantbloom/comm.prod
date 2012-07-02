#this won't do everything, you have to fill in stuff. it is just boiler plate code

from django.contrib.auth.models import User
from commProd.models import CommProd, Rating, UserProfile, ShirtName

shirtnames = ShirtName.objects.all()

for shirtname in shirtnames:
	print 'shirt id: ' + str(shirtname.id)
	shirtname.user_profile = UserProfile.objects.get(user=shirtname.user)
	shirtname.save()

ratings = Rating.objects.all()
for rating in ratings:
	print 'rating id: ' + str(rating.id)
	rating.user_profile = UserProfile.objects.get(user=rating.user)
	rating.save()

# commprods = CommProd.objects.all()

# for commprod in commprods:
# 	print commprod.id
# 	commprod.user_profile = UserProfile.objects.get(user=commprod.user)
# 	commprod.save()

