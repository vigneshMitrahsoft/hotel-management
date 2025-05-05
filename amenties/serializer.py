from rest_framework import serializers

class AmenitySerializer(serializers.Serializer):
	# amenities_id = serializers.IntegerField(read_only=True)
	amenities_name = serializers.CharField(max_length=100)
	description = serializers.CharField()
