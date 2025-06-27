from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from role.models import role

@pytest.mark.django_db
def test_get_role():
	client = APIClient()
	role.objects.create(
		role_id = 1,
		role_name = 'cleaning'
	)
	response = client.get('/api/role/list')  
	assert response.status_code == 200

@pytest.mark.django_db
def test_post_role():
	client = APIClient()
	data = {
		'role_id' : 1,
		'role_name' : 'cleaning'
	}
	response = client.post('/api/role/create', data, format='json')  
	assert response.status_code == 201 or response.status_code == 200  

@pytest.mark.django_db
def test_put_role():
	client = APIClient()
	instance = role.objects.create(
		role_id = 1,
		role_name = 'cleaning'
	)
	data = {
		'role_id' : 1,
		'role_name' : 'cleaning'
	}
	response = client.put(f'/api/role/update/{instance.pk}', data, format='json')
	assert response.status_code == 200
	instance.refresh_from_db()

@pytest.mark.django_db
def test_delete_role():
	client = APIClient()
	instance = role.objects.create(
		role_id = 1,
		role_name = 'cleaning'
	)
	response = client.delete(f'/api/role/delete/{instance.pk}')
	assert response.status_code in [200, 204, 202]