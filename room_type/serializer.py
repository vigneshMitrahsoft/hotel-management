from rest_framework import serializers
from .models import room_types

class roomTypeSerializer(serializers.Serializer):
	room_type_id = serializers.IntegerField()
	room_type = serializers.CharField(max_length = 100)
	capacity = serializers.IntegerField()
	description = serializers.CharField(max_length = 300)