from rest_framework import serializers
from .models import Hotel
 
class HotelSerializer(serializers.Serializer):
	hotel_id = serializers.IntegerField(read_only = True)
	hotel_name = serializers.CharField(max_length = 200)
	location = serializers.CharField(max_length = 200)
	email = serializers.EmailField()
	phone = serializers.CharField(max_length = 10)
	
	
	

