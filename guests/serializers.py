from rest_framework import serializers
from .models import Guests

class GuestsSerializer(serializers.Serializer):
	guest_id = serializers.IntegerField(read_only = True)
	first_name = serializers.CharField(max_length = 200)
	last_name = serializers.CharField(max_length = 200)
	email = serializers.EmailField()
	phone = serializers.CharField(max_length = 10)