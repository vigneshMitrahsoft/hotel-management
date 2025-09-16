import pytest
from rest_framework.test import APIClient
from users.models import Users

@pytest.mark.django_db
def test_get_users():
	client = APIClient()
	Users.objects.create(
		user_id = 1,
		first_name = 'kalil',
		last_name = 'fazith',
		email = 'hari@gmail.com',
		password = '123',
		phone = 9876543210
	)
	response = client.get('/api/listusers')  
	assert response.status_code == 200

@pytest.mark.django_db
def test_post_users():
	client = APIClient()
	data = {
		'user_id' : 1,
		'first_name' : 'kalil',
		'last_name' : 'fazith',
		'email' : 'hari@gmail.com',
		'password' : '123',
		'phone' : 9876543210
	}
	response = client.post('/api/adduser', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  

@pytest.mark.django_db
def test_put_users():
	client = APIClient()
	instance = Users.objects.create(
		user_id = 1,
		first_name = 'kalil',
		last_name = 'fazith',
		email = 'hari@gmail.com',
		password = '123',
		phone = 9876543210
	)
	data = {
		'user_id' : 1,
		'first_name' : 'kalil',
		'last_name' : 'fazith',
		'email' : 'hari@gmail.com',
		'password' : '123',
		'phone' : 9876543210
	}
	response = client.put(f'/api/updateuser/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()

@pytest.mark.django_db
def test_delete_users():
	client = APIClient()
	instance = Users.objects.create(
		user_id = 1
	)
	response = client.delete(f'/api/deleteuser/{instance.pk}')
	assert response.status_code in [200, 204, 202]    
