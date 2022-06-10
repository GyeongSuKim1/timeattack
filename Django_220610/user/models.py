from django.db import models


class UserModel(models.Model):
	email = models.EmailField(max_length=32, unique=True, default='')
	password = models.CharField(max_length=256,default='')

	class Meta:
		db_table = 'user'