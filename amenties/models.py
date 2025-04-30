from django.db import models

class amenities(models.Model):
	amenities_id = models.BigAutoField(primary_key=True)
	amenities_name  = models.CharField(max_length=50,blank=True,null=True)
	description = models.TextField()
	created_by = models.IntegerField(null=True)
	updated_by = models.IntegerField(null=True)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.amenities_name