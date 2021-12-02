from django.db import models

# Create your models here.


class CreateSandwichOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, default='')
    base = models.CharField(max_length=50, default='')
    meat_one = models.CharField(max_length=50, default='')
    meat_two = models.CharField(max_length=50, default='')
    cheese = models.CharField(max_length=50, default='')
    sauce = models.CharField(max_length=50, default='')
    salad = models.BooleanField(default=True)
    extra = models.CharField(max_length=150, default='')
