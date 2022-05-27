from django.shortcuts import render

# Create your views here.
class UserClass:
	def __init__(self, email, password, attribute):
		self.email = email
		self.password = password
		self.attribute = attribute