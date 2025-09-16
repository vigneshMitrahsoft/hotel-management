from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from room_type.models import room_types

@pytest.mark.django_db
def test_get_room_type():
	client = APIClient()
	room_types.objects.create(
		room_type_id = 2,
		room_type = 'deluxe',
		capacity = 8,
		description = 'available at best price'
	)
	response = client.get('/api/room_type')  
	assert response.status_code == 200
	assert response.data[0]['room_type_id'] == 2


@pytest.mark.django_db
def test_post_room_type():
	client = APIClient()
	data = {
		'room_type_id': 2,
		'room_type': 'deluxe',
		'capacity': 8,
		'description' : 'available'
	}
	response = client.post('/api/add_room_type', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  
	assert room_types.objects.count() == 1

@pytest.mark.django_db
def test_patch_room_type():
	client = APIClient()
	instance = room_types.objects.create(
		room_type_id = 2,
		room_type = 'deluxe',
		capacity = 8,
		description = 'available at best price'
	)
	data = {
		'room_type_id': 2,
		'room_type': 'deluxe',
		'capacity': 8,
		'description' : 'available'
	}
	response = client.patch(f'/api/update_room_type/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()
	assert instance.room_type_id == 2

@pytest.mark.django_db
def test_delete_room_type():
	client = APIClient()
	instance = room_types.objects.create(
		room_type_id = 2,
		room_type = 'deluxe',
		capacity = 8,
		description = 'available at best price'
	)
	response = client.delete(f'/api/delete_room_type/{instance.pk}')
	assert response.status_code in [200, 204, 202]
	assert room_types.objects.count() == 0