from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
 
@api_view(['GET','POST'])
def hotel_list(request):
	if request.method == 'GET':
		hotel = Hotel.objects.all()
		serializer = HotelSerializer(hotel, many = True)
		return Response(serializer.data, status = status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def add_hotel(request):
	serializer = HotelSerializer(data = request.data)
	if serializer.is_valid():
		Hotel.objects.create (
			hotel_name = serializer.validated_data['hotel_name'],
			location = serializer.validated_data['location'],
			email = serializer.validated_data['email'],
			phone = serializer.validated_data['phone'],
			created_by = '1'
        )
		return Response({'message' : 'Created Successfully'}, status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def update_hotel(request, pk):

	try:
		hotel = Hotel.objects.get(pk = pk)
	except Hotel.DoesNotExist:
		return Response({'error' : 'Hotel Not Found'})
	
	if request.method == 'PUT':
		serializer = HotelSerializer(data = request.data)
		if serializer.is_valid():
			hotel.hotel_name = serializer.validated_data['hotel_name']
			hotel.location = serializer.validated_data['location']
			hotel.email = serializer.validated_data['email']
			hotel.phone = serializer.validated_data['phone']
			hotel.updated_by = '1'
			hotel.save()
			return Response({'message' : 'Updated Successfully'},status = status.HTTP_200_OK)
		return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_hotel(request, pk):

	try:
		hotel = Hotel.objects.get(pk = pk)
	except Hotel.DoesNotExist:
		return Response({'error' : 'Hotel Not Found'})
	
	hotel.delete()
	return Response({'message' : 'deleted successfully'}, status = status.HTTP_400_BAD_REQUEST)






	

