from django.db import models
from ast import literal_eval

# Create your models here.
'''
	name
	description
	project_img_location
	links:
		site
		url
		link_img_location
'''
class Project(models.Model):
	name         = models.CharField(max_length = 50)
	description  = models.CharField(max_length = 500)
	img_location = models.CharField(max_length = 20)
	links		 = models.CharField(max_length = 500)

	def __str__(self):
		return self.name

	def link_list(self):
		linkList = literal_eval(self.links)
		return linkList