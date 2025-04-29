from django.db import models

class Hotel(models.Model):
	hotel_id = models.AutoField(primary_key = True)
	hotel_name = models.CharField(max_length = 100)
	location = models.CharField(max_length = 200)
	email = models.EmailField()
	phone = models.CharField(max_length = 10)
	created_at = models.DateTimeField(auto_now_add = True)
	created_by = models.CharField(max_length = 200, null = True)
	updated_at = models.DateTimeField(auto_now = True)
	updated_by = models.CharField(max_length = 200, null = True)
	
	def __str__(self):
		return self.hotel_name