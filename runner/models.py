from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=20, default='glass')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "categories"

class Drink(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category)
    volume = models.FloatField()
    abv = models.FloatField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.name + (' (' + str(self.quantity) + ')' if self.quantity > 1 else '')

    # This should handle the logic for displaying in liters, oz, gallons, etc.
    def clean_volume(self):
        return (str(int(self.volume)) if int(self.volume) == self.volume else
                self.volume) + 'oz'

    # Give an int if possible
    def clean_price(self):
        return str(int(self.price)) if int(self.price) == self.price else self.price

    class Meta:
        ordering = ('category', 'name', 'quantity', '-volume')

class Run(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    goal = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = str(self.start_date)
        super(Run, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.start_date)

    class Meta:
        ordering = ('start_date',)

class RunItem(models.Model):
    time = models.DateTimeField()
    drink = models.ForeignKey(Drink)
    run = models.ForeignKey(Run)
    customer = models.ForeignKey(User)

    def __unicode__(self):
        return self.drink.name

    class Meta:
        ordering = ('time',)
