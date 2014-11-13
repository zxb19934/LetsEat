#encoding:utf-8
from django.db import models

class ShopKeeperModel(models.Model):
	'''店长'''
	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	account = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
	shop = models.OneToOneField(ShopModel,related_name = "shopkeeper_shop")

class ShopModel(models.Model):
	'''店铺'''
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	shoptype = models.CharField(max_length=15)
	miniprice = models.FloatField()
	announcement = models.CharField(max_length=200)
	status = models.CharField(max_length=5)

class CuisineModel(models.Model):
	'''菜式'''
	name = models.CharField(max_length=20)
	price = models.FloatField()
	grade = models.FloatField()
	salesvolume = models.PositiveSmallIntegerField()
	shop = models.ForeignKey(ShopKeeperModel,related_name = "cuisine_shop")
