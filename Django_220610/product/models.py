from django.db import models


# Create your models here.

class ProductModel(models.Model):
	name = models.CharField(max_length=32)
	category = models.CharField(max_length=200)
	image = models.CharField(max_length=200)
	info = models.TextField(max_length=300)
	price = models.IntegerField()
	stock = models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Product'


class OrderStatusModel(models.Model):
	category = models.ForeignKey('ProductModel', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'OrderStatus'