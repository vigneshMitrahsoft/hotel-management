from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from guests.models import Guests

@pytest.mark.django_db
def test_get_guests():
	client = APIClient()
	Guests.objects.create(
		first_name = 'kalil',
		last_name = 'fazith',
		email = 'kalil@gmail.com',
		phone = '9087654321'
	)
	response = client.get('/api/listguests')  
	assert response.status_code == 200

@pytest.mark.django_db
def test_post_guests():
	client = APIClient()
	data = {
		'first_name' : 'kalil',
		'last_name' : 'fazith',
		'email' : 'kalil@gmail.com',
		'phone' : '9087654321'
	}
	response = client.post('/api/addguest', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  

@pytest.mark.django_db
def test_put_guests():
	client = APIClient()
	instance = Guests.objects.create(
		first_name = 'kalil',
		last_name = 'fazith',
		email = 'kalil@gmail.com',
		phone = '9087654321'
	)
	data = {
		'first_name' : 'kalil',
		'last_name' : 'fazith',
		'email' : 'kalil@gmail.com',
		'phone' : '9087654321'
	}
	response = client.put(f'/api/updateguest/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()

@pytest.mark.django_db
def test_delete_guests():
	client = APIClient()
	instance = Guests.objects.create(
		first_name = 'kalil',
		last_name = 'fazith',
		email = 'kalil@gmail.com',
		phone = '9087654321'
	)
	response = client.delete(f'/api/deleteguest/{instance.pk}')
	assert response.status_code in [200, 204, 202]