from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Guests
from .serializers import GuestsSerializer
from rest_framework.exceptions import APIException 
 
@api_view(['GET'])
def guests_list(request):
		user = Guests.objects.all()
		serializer = GuestsSerializer(user, many = True)
		return Response(serializer.data, status = status.HTTP_200_OK)
    
@api_view(['POST'])
def add_guest(request):
	serializer = GuestsSerializer(data = request.data)
	if serializer.is_valid():
		Guests.objects.create (
			first_name = serializer.validated_data['first_name'],
			last_name = serializer.validated_data['last_name'],
			email = serializer.validated_data['email'],
			phone = serializer.validated_data['phone'],
			created_by = '1'
        )
		return Response({'message' : 'Created Successfully'}, status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

def get_guest_id(pk):
	try:
		guest = Guests.objects.get(guest_id = pk)
	except Guests.DoesNotExist:
		raise APIException("Guest does not exist")
	return guest

@api_view(['PUT'])
def update_guest(request, pk):
	guest = get_guest_id(pk)
	serializer = GuestsSerializer(guest, data = request.data, partial = True)
	if serializer.is_valid():
		guest.first_name = serializer.validated_data['first_name']
		guest.last_name = serializer.validated_data['last_name']
		guest.email = serializer.validated_data['email']
		guest.phone = serializer.validated_data['phone']
		guest.updated_by = '1'
		guest.save()
		return Response({'message' : 'Updated Successfully'},status = status.HTTP_200_OK)
	return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_guest(request, pk):
	try:
		guest = Guests.objects.get(pk = pk)
		guest.delete()
		return Response({'message' : 'deleted successfully'}, status = status.HTTP_200_OK)
	except Guests.DoesNotExist:
		return Response({'error' : 'Guest Not Found'})
