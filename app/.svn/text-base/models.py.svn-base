from django.db import models

# Create your models here.

class Administrator(models.Model):
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.username

class Distribute(models.Model):
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 65536)

	def __unicode__(self):
		return self.title
