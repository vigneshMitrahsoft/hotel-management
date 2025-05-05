from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import role
from .serializer import roleSerializer
from rest_framework.exceptions import APIException

@api_view(['POST'])
def create_role(request):
	serializer = roleSerializer(data = request.data)
	if serializer.is_valid():
		role.objects.create(
			role_id = serializer.validated_data['role_id'],
			role_name = serializer.validated_data['role_name'],
			created_by = 1,
			updated_by = 1
		)
		return Response({'message': 'Role created successfully'}, status = status.HTTP_201_CREATED)
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_roles(request):
	roles = role.objects.all()
	serializer = roleSerializer(roles, many=True)
	return Response(serializer.data)

def get_role(pk):
	try:
		Role = role.objects.get(role_id = pk)
	except:
		raise APIException("role not Available")
	return Role

@api_view(['PUT'])
def update_role(request, pk):
	role = get_role(pk = pk)
	serializer = roleSerializer(data = request.data)
	if serializer.is_valid():
		role.role_name = serializer.validated_data['role_name']
		role.updated_by = 1
		role.save()
		return Response({'message': 'Role updated successfully'})
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_role(request, pk):
	role = get_role(pk = pk)
	role.delete()
	return Response({'message': 'Role deleted successfully'})



