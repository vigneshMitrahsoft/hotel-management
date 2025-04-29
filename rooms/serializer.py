from rest_framework import serializers
from .models import rooms

class roomSerializer(serializers.Serializer):
	room_number = serializers.IntegerField()
	status = serializers.CharField(max_length = 100)
	price = serializers.DecimalField(max_digits = 5, decimal_places = 2)