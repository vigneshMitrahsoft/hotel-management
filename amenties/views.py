from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import amenities
from .serializer import  AmenitySerializer
from rest_framework.exceptions import APIException


@api_view(['POST'])
def create_amenity(request):
    serializer = AmenitySerializer(data = request.data)
    if serializer.is_valid():
        amenities.objects.create(
            amenities_id = serializer.validated_data['amenities_id'], 
            amenities_name = serializer.validated_data['amenities_name '],
            created_by = 2,
            updated_by = 3
        )
        return Response({'message': 'Amenity created successfully'}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_amenties(request):
	Amentites = amenities.objects.all()
	serializer = AmenitySerializer(Amentites, many=True)
	return Response(serializer.data)


def get_amenties(pk):
	try:
		Amenties = amenities.objects.get(amenities_id = pk)
	except:
		raise APIException("Amenties are not Available")
	return Amenties

@api_view(['PUT'])
def update_amenity(request, pk):
    amenities = get_amenties(pk = pk)
    serializer = AmenitySerializer(data = request.data)
    if serializer.is_valid():
        amenities.amenities_name = serializer.validated_data['amenities_name ']
        amenities.save()
        return Response({'message': 'Amenity updated successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_amenity(request, pk):
    amenity = get_amenties(pk = pk)
    amenity.delete()
    return Response({'message': 'Amenity deleted successfully'})

