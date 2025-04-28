from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  Staff
from .serializer import  StaffSerializer
from django.shortcuts import get_object_or_404




@api_view(['POST'])
def create_staff(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        
        Staff.objects.create(
            staff_id=serializer.validated_data['staff_id'],
            staff_name=serializer.validated_data['staff_name'],
            email=serializer.validated_data['email'],
            phone=serializer.validated_data['phone'],
            role_id=serializer.validated_data['role_id'],
            hotel_id= serializer.validated_data['hotel_id'],
            created_by=1,
            updated_by=2
        )
        return Response({'message': 'Staff created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_staff(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    serializer = StaffSerializer(staff)
    return Response(serializer.data)

@api_view(['PUT'])
def update_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        staff.staff_id=serializer.validated_data['staff_id']
      
        staff.staff_name = serializer.validated_data['staff_name']
        staff.email=serializer.validated_data['email']
        staff.phone=serializer.validated_data['phone']
        staff.role_id=serializer.validated_data['role_id']
        staff.hotel_id= serializer.validated_data['hotel_id']
        staff.created_by=1
        staff.updated_by=1
       
       
        staff.save()
        return Response({'message': 'Staff updated successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    return Response({'message': 'Staff deleted successfully'})

