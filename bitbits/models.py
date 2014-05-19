from django.db import models

class Items(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=26, decimal_places=2)
	imgfile = models.CharField(max_length=100)
