from django.contrib import admin
from runner.models import Category, Drink, Run, RunItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(Run)
admin.site.register(RunItem)
