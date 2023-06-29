from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.TextField(max_length=50)
    category = models.TextField(max_length=50)
    quantity = models.IntegerField()
    acquisition_price = models.FloatField(null=True)
    sell_price = models.FloatField()
    discount = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(default=0)
    supplier = models.TextField(max_length=50, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    sold_quantity = models.IntegerField(default=0)