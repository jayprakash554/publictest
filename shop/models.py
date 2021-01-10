from django.db import models

# Create your models here.
class Mytb(models.Model):
	username = models.CharField(max_length = 100)
class Myupload(models.Model):
	username = models.CharField(max_length = 100)
	picture = models.FileField()
