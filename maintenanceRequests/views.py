from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import maintenanceRequests
from .serializer import requestsSerializer
from rest_framework.exceptions import APIException

@api_view(('GET',))
def list_requests(request):
	requests = maintenanceRequests.objects.all()
	serializer = requestsSerializer(requests, many = True)
	return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(('POST',))
def add_requests(request):
	serializer = requestsSerializer(data = request.data)
	if serializer.is_valid():
		maintenanceRequests.objects.create(
			guest_id = serializer.validated_data['guest_id'],
			request_for = serializer.validated_data['request_for'],
			status = serializer.validated_data['status'],
			requested_on = serializer.validated_data['requested_on'],
			resolved_on = serializer.validated_data['resolved_on'],
			resolved_by = serializer.validated_data['resolved_by'],
			created_by = 1
		)
		return Response(status = status.HTTP_201_CREATED)
	return Response(status = status.HTTP_400_BAD_REQUEST)

def check_requests(pk):
	try:
		room_type = maintenanceRequests.objects.get(pk = pk)
	except maintenanceRequests.DoesNotExist:
		raise APIException(detail = {"statuscode" : 404, "status" : "error", "message" : "room not found"})
	return room_type

@api_view(('PATCH',))
def update_requests(request, pk):
	requests = check_requests(pk = pk)
	serializer = requestsSerializer(requests, data = request.data)
	if serializer.is_valid():
		requests.request_for = serializer.validated_data['request_for']
		requests.status = serializer.validated_data['status']
		requests.requested_on = serializer.validated_data['requested_on']
		requests.resolved_on = serializer.validated_data['resolved_on']
		requests.resolved_by = serializer.validated_data['resolved_by']
		requests.updated_by = 2
		requests.save()
		return Response("{'message' : 'updated successfully'}")
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('DELETE',))
def delete_requests(request, pk):
	requests = check_requests(pk)
	requests.delete()
	return Response(status = status.HTTP_202_ACCEPTED)