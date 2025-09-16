from django.db import models

# Create your models here.
class room_types(models.Model):
	room_type_id = models.IntegerField(primary_key = True)
	room_type = models.CharField(max_length = 100)
	capacity = models.IntegerField()
	description = models.TextField(max_length=200)
	created_at = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)
	updated_by = models.CharField(max_length=100, null = True)
	created_by = models.CharField(max_length=100, null = True)

	class Meta:
		db_table = 'room_type'