from rest_framework import serializers

class StaffSerializer(serializers.Serializer):
    staff_id=serializers.IntegerField()
    staff_name=serializers.CharField(max_length=150)
    email=serializers.EmailField()
    phone=serializers.IntegerField()
    role_id=serializers.IntegerField()
    hotel_id=serializers.IntegerField()
