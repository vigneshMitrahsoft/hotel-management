import pytest
from rest_framework.test import APIClient
from maintenanceRequests.models import maintenanceRequests

@pytest.mark.django_db
def test_get_requests():
	client = APIClient()
	maintenanceRequests.objects.create(
		guest_id = 1,
		request_for = 'food',
		status = 'completed',
		requested_on = '2025-05-05',
		resolved_on = '2025-05-05',
		resolved_by = 1
	)
	response = client.get('/api/requests')  
	assert response.status_code == 200

@pytest.mark.django_db
def test_post_requests():
	client = APIClient()
	data = {
		'guest_id' : 1,
		'request_for' : 'food',
		'status' : 'completed',
		'requested_on' : '2025-05-05',
		'resolved_on' : '2025-05-05',
		'resolved_by' : 1
	}
	response = client.post('/api/add_requests', data, format='json')  
	assert response.status_code == 201 

@pytest.mark.django_db
def test_patch_requests():
	client = APIClient()
	instance = maintenanceRequests.objects.create(
		guest_id = 1,
		request_for = 'food',
		status = 'completed',
		requested_on = '2025-05-05',
		resolved_on = '2025-05-05',
		resolved_by = 1
	)
	data = {
		'guest_id' : 1,
		'request_for' : 'food',
		'status' : 'completed',
		'requested_on' : '2025-05-05',
		'resolved_on' : '2025-05-05',
		'resolved_by' : 1
	}
	response = client.patch(f'/api/update_requests/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()

@pytest.mark.django_db
def test_delete_requests():
	client = APIClient()
	instance = maintenanceRequests.objects.create(
		guest_id = 1,
		request_for = 'food',
		status = 'completed',
		requested_on = '2025-05-05',
		resolved_on = '2025-05-05',
		resolved_by = 1
	)
	response = client.delete(f'/api/delete_requests/{instance.pk}')
	assert response.status_code in [200, 204, 202]
 

