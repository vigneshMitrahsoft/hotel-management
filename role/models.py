from django.db import models

class role(models.Model):
	role_id = models.IntegerField(primary_key = True)
	role_name = models.CharField(max_length = 50, blank = True, null = True)
	created_at = models.DateField(auto_now = True)
	updated_at = models.DateField(auto_now = True)
	created_by = models.IntegerField(null = True)
	updated_by = models.IntegerField(null = True)

	def __str__(self):
		return self.role_name

