from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from room_amenties.models import room_amenties

@pytest.mark.django_db
def test_post_room_amenities():
	client = APIClient()
	data = {
		# 'room' : 101,
		# 'amenties' : 'TV'
	}
	response = client.post('/api/room_amenties/create', data, format='json')  
	assert response.status_code == 400 

@pytest.mark.django_db
def test_put_room_amenties():
	client = APIClient()
	instance = room_amenties.objects.create(
		# room = 101,
		# amenties = 'TV'
	)
	data = {
		# 'room' : 101,
		# 'amenties' : 'TV'
	}
	response = client.put(f'/api/room_amenties/update/{instance.pk}', data, format='json')
	assert response.status_code == 400
	instance.refresh_from_db()
