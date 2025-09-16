from django.db import models
from guests.models import Guests
from staff_role.models import Staff

class maintenanceRequests(models.Model):
	guest_id = models.IntegerField(primary_key = True)
	request_for = models.CharField(max_length=20)
	status = models.CharField(max_length = 100)
	requested_on = models.DateField()
	resolved_on = models.DateField()
	resolved_by = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)
	updated_by = models.CharField(max_length = 100, null = True)
	created_by = models.CharField(max_length = 100, null = True)
 
	class Meta:
		db_table = 'maintenance_requests'