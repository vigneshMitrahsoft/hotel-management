from django.db import models
class rooms(models.Model):
	room_number = models.IntegerField()
	status = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits = 7, decimal_places = 2)
	created_at = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)
	updated_by = models.CharField(max_length=100, null = True, default = 1)
	created_by = models.CharField(max_length=100, null = True, default = 1)
	class Meta:
		db_table = 'rooms'
