from django.db import models

class Administrator(models.Model):
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.username

class Distribute(models.Model):
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 65536)
	category = models.CharField(max_length = 10)
	tag = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.name
