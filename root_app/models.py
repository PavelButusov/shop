# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Shop(models.Model):
    pass


class Product(models.Model):
    category = models.ManyToManyField('Category')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2048)
    price = models.FloatField(default=1.)

    def __str__(self):
        return '%s($%s)' % (self.title, self.price)

    def __unicode__(self):
        return self.title


class Cart(models.Model):
    profile = models.ForeignKey('Profile')
    products = models.ManyToManyField('BasketedProduct')


class Profile(models.Model):
    email = models.EmailField()


class Order(models.Model):
    # В чём разница между корзиной и заказом?..
    product = models.ManyToManyField('BasketedProduct')


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class BasketedProduct(models.Model):
    product = models.ForeignKey('Product')
    profile = models.ForeignKey('Profile')
    bought = models.BooleanField(default=False)
