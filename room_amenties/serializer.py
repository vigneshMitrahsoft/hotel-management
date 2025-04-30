from rest_framework import serializers
from rooms.models import rooms
from amenties.models import amenities
from .models import room_amenties

class RoomAmentiesSerializer(serializers.Serializer):
	room_amenties_id = serializers.IntegerField(read_only=True)
	room = serializers.PrimaryKeyRelatedField(queryset = rooms.objects.all(),required=True)
	amenties = serializers.PrimaryKeyRelatedField(queryset = amenities.objects.all(),required=True)
	created_by = serializers.IntegerField(required = False)
	updated_by = serializers.IntegerField(required = False)
	created_at = serializers.DateTimeField(read_only = True)
	updated_at = serializers.DateTimeField(read_only = True)
	is_active = serializers.BooleanField(default = True)
	is_deleted = serializers.BooleanField(default = False)

	def create(self, validated_data):
		return room_amenties.objects.create(**validated_data)

	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			setattr(instance, attr, value)
		instance.save()
		return instance