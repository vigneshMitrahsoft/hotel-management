from rest_framework import serializers

class roleSerializer(serializers.Serializer):
    role_id = serializers.IntegerField()
    role_name = serializers.CharField(max_length = 150)
    