from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=20, default='glass')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "categories"

volume_conversions = {
    '169.1oz': '5L',
    '101.4oz': '3L',
    '59.2oz': '1.75L',
    '33.8oz': '1L',
    '25.4oz': '750mL'
}

class Drink(models.Model):
    name = models.CharField(max_length=60)
    category = models.ManyToManyField(Category, blank=True)
    volume = models.FloatField()
    abv = models.FloatField()
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.name + (' (' + str(self.quantity) + ')' if self.quantity > 1 else '')

    # This should handle the logic for displaying in liters, oz, gallons, etc.
    def clean_volume(self):
        prestr = (str(int(self.volume)) if int(self.volume) == self.volume else
                str(self.volume)) + 'oz'
        if prestr in volume_conversions:
            return volume_conversions[prestr]
        return prestr

    # Give an int if possible
    def clean_price(self):
        return str(int(self.price)) if int(self.price) == self.price else str(self.price)

    class Meta:
        ordering = ('name', 'quantity', '-volume')

class Run(models.Model):
    start_time = models.DateTimeField(default=datetime.datetime.now())
    end_time = models.DateTimeField(null=True, blank=True)
    goal = models.DecimalField(max_digits=6, decimal_places=2, default=500.00)
    name = models.CharField(max_length=200)
    run_master = models.CharField(max_length=200, default='runmasters@mit.edu')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = 'Run ' + str(self.start_time)
        super(Run, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.start_time)

    def total_price(self):
        items = RunItem.objects.filter(run=self)
        return sum(map(lambda i: i.drink.price, items))

    class Meta:
        ordering = ('end_time', 'start_time')

class RunItem(models.Model):
    time = models.DateTimeField()
    drink = models.ForeignKey(Drink)
    run = models.ForeignKey(Run)
    customer = models.ForeignKey(User)

    def __unicode__(self):
        return self.drink.name

    class Meta:
        ordering = ('time',)

