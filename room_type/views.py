from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import room_types
from .serializer import roomTypeSerializer
from rest_framework.exceptions import APIException

@api_view(('GET',))
def list_room_type(request):
	room_type = room_types.objects.all()
	serializer = roomTypeSerializer(room_type, many = True)
	return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(('POST',))
def add_room_type(request):
	serializer = roomTypeSerializer(data = request.data)
	if serializer.is_valid():
		room_types.objects.create(
			room_type_id = serializer.validated_data['room_type_id'],
			room_type = serializer.validated_data['room_type'],
			capacity = serializer.validated_data['capacity'],
			description = serializer.validated_data['description'],
			created_by = 1
		)
		return Response(status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

def check_room_type(pk):
	try:
		room_type = room_types.objects.get(pk = pk)
	except room_types.DoesNotExist:
		raise APIException(detail = {"statuscode" : 404, "status" : "error", "message" : "room not found"})
	return room_type

@api_view(('PATCH',))
def update_room_type(request, pk):
	room_type = check_room_type(pk = pk)
	serializer = roomTypeSerializer(room_type, data = request.data)
	if serializer.is_valid():
		room_type.room_type_id = serializer.validated_data['room_type_id']
		room_type.room_type = serializer.validated_data['room_type']
		room_type.capacity = serializer.validated_data['capacity']
		room_type.description = serializer.validated_data['description']
		room_type.updated_by = 2
		room_type.save()
		return Response("{'message' : 'updated successfully'}")
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('DELETE',))
def delete_room_type(request, pk):
	room_type = check_room_type(pk)
	room_type.delete()
	return Response(status = status.HTTP_202_ACCEPTED)