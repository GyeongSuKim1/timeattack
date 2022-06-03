from django.db import models


# Create your models here.
class DrinkModel(models.Model):
	class Meta:
		db_table = "drink"

	nutrition_info = models.CharField(max_length=256)
	allergy = models.CharField(max_length=256)


class DrinkCategory(models.Model):
	class Meta:
		db_table = "category"

	drink = models.ForeignKey(DrinkModel, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	nutrition_info = drink.nutrition_info
	allergy = drink.allergy
