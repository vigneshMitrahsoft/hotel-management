from django.db import models

class Guests(models.Model):
	guest_id = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField()
	phone = models.CharField(max_length = 10)
	created_at = models.DateTimeField(auto_now_add = True)
	created_by = models.CharField(max_length = 200, null = True)
	updated_at = models.DateTimeField(auto_now = True)
	updated_by = models.CharField(max_length = 200, null = True)
