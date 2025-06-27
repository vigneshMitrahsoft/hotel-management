from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from hotel.models import Hotel
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

@pytest.mark.django_db
def test_get_hotel():
	client = APIClient()
	Hotel.objects.create(
		hotel_id = 1,
		hotel_name = 'star',
		location = 'madurai',
		email = 'star@gmail.com',
		phone = '9876543210'
	)
	response = client.get('/api/hotellist')  
	assert response.status_code == 200
	assert response.data[0]['hotel_id'] == 1

@pytest.mark.django_db
def test_post_hotel():
	client = APIClient()
	data = {
		'hotel_id' : 1,
		'hotel_name' : 'star',
		'location' : 'madurai',
		'email' : 'star@gmail.com',
		'phone' : '9876543210'
	}
	response = client.post('/api/addhotel', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  
	assert Hotel.objects.count() == 1

@pytest.mark.django_db
def test_put_hotel():
	client = APIClient()
	instance = Hotel.objects.create(
		hotel_id = 1,
		hotel_name = 'star',
		location = 'madurai',
		email = 'star@gmail.com',
		phone = '9876543210'
	)
	data = {
		'hotel_id' : 1,
		'hotel_name' : 'star',
		'location' : 'madurai',
		'email' : 'star@gmail.com',
		'phone' : '9876543210'
	}
	response = client.put(f'/api/updatehotel/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()
	assert instance.hotel_id == 1

@pytest.mark.django_db
def test_delete_hotel():
	client = APIClient()
	instance = Hotel.objects.create(
		hotel_id = 1,
		hotel_name = 'star',
		location = 'madurai',
		email = 'star@gmail.com',
		phone = '9876543210'
	)
	response = client.delete(f'/api/deletehotel/{instance.pk}')
	assert response.status_code in [200, 204, 202]
	assert Hotel.objects.count() == 0