from django.db import models

class amenities(models.Model):
	amenities_id = models.IntegerField(primary_key=True)
	amenities_name  = models.CharField(max_length=50,blank=True,null=True)
	description = models.TextField()

	def __str__(self):
		return self.amenities_name
