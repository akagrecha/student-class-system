from __future__ import unicode_literals

from django.db import models

class student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	marks1 = models.IntegerField()
	marks2 = models.IntegerField()
	marks3 = models.IntegerField()
