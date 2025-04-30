from django.db import models
from rooms.models import rooms
from amenties.models import amenities

class room_amenties(models.Model):
	room_amenties_id = models.BigAutoField(primary_key = True)
	room = models.ForeignKey(rooms, on_delete = models.DO_NOTHING, blank = True,null = True)
	amenties = models.ForeignKey(amenities, on_delete = models.DO_NOTHING, blank = True,null = True)
	created_by = models.IntegerField(null = True)
	updated_by = models.IntegerField(null = True)
	created_at = models.DateTimeField(auto_now = True)
	updated_at = models.DateTimeField(auto_now = True)
	is_active = models.BooleanField(default = True)
	is_deleted = models.BooleanField(default = False)
	
	class Meta:
		db_table = "room_amenties"