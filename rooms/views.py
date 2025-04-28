import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import rooms
from .serializer import roomSerializer
from rest_framework.exceptions import APIException

# Create your views here.
@api_view(['GET', 'POST'])
def room_list(request):
	if request.method == 'GET':
		room = rooms.objects.all()
		serializer = roomSerializer(room, many = True)    
		return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
def addroom(request):
    if request.method == 'POST':
        serializer = roomSerializer(data = request.data)
        if serializer.is_valid():
            rooms.objects.create(
                room_number = serializer.validated_data['room_number'],
                status = serializer.validated_data['status'],
                price = serializer.validated_data['price']
		    )
        return Response(status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

def check_room(pk):
    try:
        room = rooms.objects.get(pk = pk)
    except rooms.DoesNotExist:
        raise APIException(detail = {"statuscode": 404, "status":"error", "message": "room not found"})
    return room

@api_view(['PATCH'])
def updateroom(request, pk):
    room = check_room(pk)
    serializer = roomSerializer(room, data = request.data, partial = True)
    if serializer.is_valid():
        rooms.objects.filter(pk = pk).update(**serializer.validated_data)
        return Response({"statuscode" : status.HTTP_200_OK, "status" : "success"}, status = status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteroom(request,pk):
    room = get_object_or_404(rooms, pk = pk)
    room.delete()
    return Response(status = status.HTTP_202_ACCEPTED)



	