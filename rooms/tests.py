import pytest
from rest_framework.test import APIClient
from rooms.models import rooms

@pytest.mark.django_db
def test_get_rooms():
	client = APIClient()
	rooms.objects.create(
		room_number=101,
		status='available',
		price='900.00'
	)
	response = client.get('/api/rooms')  
	assert response.status_code == 200
	assert response.data[0]['room_number'] == 101

@pytest.mark.django_db
def test_post_rooms():
	client = APIClient()
	data = {
		'room_number': 102,
		'status': 'available',
		'price': '500.00'
	}
	response = client.post('/api/add_room', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  
	assert rooms.objects.count() == 1

@pytest.mark.django_db
def test_patch_rooms():
	client = APIClient()
	instance = rooms.objects.create(
		room_number=103,
		status='available',
		price='900.00'
	)
	data = {
		'room_number': instance.room_number,
		'status': 'occupied',
		'price': instance.price
	}
	response = client.patch(f'/api/update_room/{instance.id}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()
	assert instance.status == 'occupied'

@pytest.mark.django_db
def test_delete_rooms():
	client = APIClient()
	instance = rooms.objects.create(
		room_number=104,
		status='available',
		price= 900.00
	)
	response = client.delete(f'/api/delete_room/{instance.pk}')
	assert response.status_code in [200, 204, 202]    
	assert rooms.objects.count() == 0