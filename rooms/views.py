from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import rooms
from .serializer import roomSerializer
from rest_framework.exceptions import APIException

@api_view(('GET',))
def list_room(request):
	room = rooms.objects.all()
	serializer = roomSerializer(room, many = True)	
	return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(('POST',))
def add_room(request):
	serializer = roomSerializer(data = request.data)
	if serializer.is_valid():
		rooms.objects.create(
			room_number = serializer.validated_data['room_number'],
			status = serializer.validated_data['status'],
			price = serializer.validated_data['price']
		)
		return Response(status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

def check_room(id):
	try:
		room = rooms.objects.get(id = id)
	except rooms.DoesNotExist:
		raise APIException(detail = {"statuscode" : 404, "status" : "error", "message" : "room not found"})
	return room

@api_view(('PATCH',))
def update_room(request, id):
	room = check_room(id)
	serializer = roomSerializer(room, data = request.data)
	if serializer.is_valid():
		room.room_number = serializer.validated_data['room_number']
		room.status = serializer.validated_data['status']
		room.price = serializer.validated_data['price']
		room.updated_by = 2
		room.save()
		return Response("{'message' : 'updated successfully'}")
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('DELETE',))
def delete_room(request, pk):
	room = check_room(pk)
	room.delete()
	return Response(status = status.HTTP_202_ACCEPTED)