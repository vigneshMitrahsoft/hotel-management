from rest_framework import serializers
from .models import maintenance_requests

class requestsSerializer(serializers.Serializer):
	user_id = serializers.IntegerField()
	request_for = serializers.CharField(max_length=20)
	status = serializers.CharField(max_length = 100)
	requested_on = serializers.DateField()
	resolved_on = serializers.DateField()
	resolved_by = serializers.IntegerField()