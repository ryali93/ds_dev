from django.db import models

class Review(models.Model):
	review = models.TextField(max_length=4000)
	
