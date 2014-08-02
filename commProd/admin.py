import commProd.models as cpm
from django.contrib import admin

admin.site.register(cpm.UserProfile)
admin.site.register(cpm.Email)
admin.site.register(cpm.PasswordReset)
admin.site.register(cpm.ShirtName)
admin.site.register(cpm.CommProd)
admin.site.register(cpm.CommProdEmail)
admin.site.register(cpm.Rating)
admin.site.register(cpm.TrendData)
admin.site.register(cpm.Correction)
admin.site.register(cpm.CorrectionRating)
admin.site.register(cpm.Favorite)