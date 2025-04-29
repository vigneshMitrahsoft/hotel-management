from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.Serializer):
	user_id = serializers.IntegerField(read_only = True)
	first_name = serializers.CharField(max_length = 200)
	last_name = serializers.CharField(max_length = 200)
	email = serializers.EmailField()
	password = serializers.CharField(max_length = 50)
	phone = serializers.CharField(max_length = 10)