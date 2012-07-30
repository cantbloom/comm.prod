from commProd.models import UserProfile, Email, ShirtName, CommProd, CommProdEmail, Rating, TrendData, Correction, CorrectionRating, PasswordReset
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Email)
admin.site.register(PasswordReset)
admin.site.register(ShirtName)
admin.site.register(CommProd)
admin.site.register(CommProdEmail)
admin.site.register(Rating)
admin.site.register(TrendData)
admin.site.register(Correction)
admin.site.register(CorrectionRating)