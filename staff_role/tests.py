import pytest
from rest_framework.test import APIClient
from staff_role.models import Staff

@pytest.mark.django_db
def test_get_staff():
	client = APIClient()
	Staff.objects.create(
		staff_id = 1,
		staff_name = 'hari',
		email = 'hari@gmail.com',
		phone = 9876543210,
		role_id = 1,
		hotel_id = 1
	)
	response = client.get('/api/staffs/list')  
	assert response.status_code == 200

@pytest.mark.django_db
def test_post_staff():
	client = APIClient()
	data = {
		'staff_id' : 1,
		'staff_name' : 'hari',
		'email' : 'hari@gmail.com',
		'phone' : 9876543210,
		'role_id' : 1,
		'hotel_id' : 1
	}
	response = client.post('/api/staffs/create', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  

@pytest.mark.django_db
def test_put_staff():
	client = APIClient()
	instance = Staff.objects.create(
		staff_id = 1,
		staff_name = 'hari',
		email = 'hari@gmail.com',
		phone = 9876543210,
		role_id = 1,
		hotel_id = 1
	)
	data = {
		'staff_id' : 1,
		'staff_name' : 'hari',
		'email' : 'hari@gmail.com',
		'phone' : 9876543210,
		'role_id' : 1,
		'hotel_id' : 1
	}
	response = client.put(f'/api/staffs/update/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()

@pytest.mark.django_db
def test_delete_staff():
	client = APIClient()
	instance = Staff.objects.create(
		staff_id = 1,
		staff_name = 'hari',
		email = 'hari@gmail.com',
		phone = 9876543210,
		role_id = 1,
		hotel_id = 1
	)
	response = client.delete(f'/api/staffs/delete/{instance.pk}')
	assert response.status_code in [200, 204, 202]    
