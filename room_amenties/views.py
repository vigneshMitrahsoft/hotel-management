from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import room_amenties
from .serializer import RoomAmentiesSerializer

@api_view(['POST'])
def create_room_amenties(request):
    serializer = RoomAmentiesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_room_amenties(request, pk):
    try:
        instance = room_amenties.objects.get(pk=pk, is_deleted=False)
    except room_amenties.DoesNotExist:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RoomAmentiesSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)