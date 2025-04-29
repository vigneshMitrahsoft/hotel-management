from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UsersSerializer
from rest_framework.exceptions import APIException 
 
@api_view(['GET'])
def users_list(request):
		user = Users.objects.all()
		serializer = UsersSerializer(user, many = True)
		return Response(serializer.data, status = status.HTTP_200_OK)
    
@api_view(['POST'])
def add_users(request):
	serializer = UsersSerializer(data = request.data)
	if serializer.is_valid():
		Users.objects.create (
			first_name = serializer.validated_data['first_name'],
			last_name = serializer.validated_data['last_name'],
			email = serializer.validated_data['email'],
			password = serializer.validated_data['password'],
			phone = serializer.validated_data['phone'],
			created_by = '1'
        )
		return Response({'message' : 'Created Successfully'}, status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

def get_user_id(pk):
	try:
		user = Users.objects.get(user_id = pk)
	except Users.DoesNotExist:
		raise APIException("Hotel does not exist")
	return user

@api_view(['PUT'])
def update_users(request, pk):
	user = get_user_id(pk)
	serializer = UsersSerializer(user, data = request.data, partial = True)
	if serializer.is_valid():
		user.first_name = serializer.validated_data['first_name']
		user.last_name = serializer.validated_data['last_name']
		user.email = serializer.validated_data['email']
		user.password = serializer.validated_data['password']
		user.phone = serializer.validated_data['phone']
		user.updated_by = '1'
		user.save()
		return Response({'message' : 'Updated Successfully'},status = status.HTTP_200_OK)
	return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_users(request, pk):
	try:
		user = Users.objects.get(pk = pk)
		user.delete()
		return Response({'message' : 'deleted successfully'}, status = status.HTTP_200_OK)
	except Users.DoesNotExist:
		return Response({'error' : 'Hotel Not Found'})