from rest_framework import serializers

class StaffSerializer(serializers.Serializer):
    staff_id=serializers.IntegerField()
    staff_name=serializers.CharField(max_length=150)
    email=serializers.EmailField()
    phone=serializers.IntegerField()
    role_id=serializers.IntegerField()
    hotel_id=serializers.IntegerField()
    

# class StaffSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     role = serializers.IntegerField()

# class AmenitySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)

# class RoomAmenitySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     room_number = serializers.CharField(max_length=10)
#     amenity = serializers.IntegerField()
