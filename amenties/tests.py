# from django.test import TestCase
# import pytest
# from rest_framework.test import APIClient
# from amenties.models import amenities

# @pytest.mark.django_db
# def test_get_amenities():
# 	client = APIClient()
# 	amenities.objects.create(
# 		amenities_name = 'wifi',
# 		description = 'all facilities available'
# 	)
# 	response = client.get('/api/amenties/list')  
# 	assert response.status_code == 200

# @pytest.mark.django_db
# def test_post_amenities():
# 	client = APIClient()
# 	data = {
# 		'amenities_name' : 'wifi',
# 		'description' : 'all facilities available'
# 	}
# 	response = client.post('/api/amenties/create', data, format='json')  
# 	assert response.status_code == 201 or response.status_code == 200  

# @pytest.mark.django_db
# def test_put_amenties():
# 	client = APIClient()
# 	instance = amenities.objects.create(
# 		amenities_name = 'wifi',
# 		description = 'all facilities available'
# 	)
# 	data = {
# 		'amenities_name' : 'wifi',
# 		'description' : 'all facilities available'
# 	}
# 	response = client.put(f'/api/amenties/update/{instance.pk}', data, format='json')
# 	assert response.status_code == 200
# 	instance.refresh_from_db()

# @pytest.mark.django_db
# def test_delete_amenties():
# 	client = APIClient()
# 	instance = amenities.objects.create(
# 		amenities_name = 'wifi',
# 		description = 'all facilities available'
# 	)
# 	response = client.delete(f'/api/amenties/delete/{instance.pk}')
# 	assert response.status_code in [200, 204, 202]

from django.test import TestCase
from .models import amenities

class MyModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		amenities.objects.create(amenities_name = 'tv', description = 'available')

	def test_create_model(self):
		new_object = amenities.objects.create(amenities_name = 'tv', description = 'available')
		self.assertEqual(new_object.amenities_name, 'tv')
		self.assertEqual(new_object.description, 'available')
	
	def test_update_model(self):
		object_to_update = amenities.objects.get(amenities_name = 'tv')
		object_to_update.amenities_name = 'wifi'
		object_to_update.description = 'available'
		object_to_update.save()
		self.assertEqual(object_to_update.amenities_name, 'wifi')
		self.assertEqual(object_to_update.description, 'available')

	def test_delete_model(self):
		object_to_delete = amenities.objects.get(amenities_name = 'tv')
		object_to_delete.delete()
		self.assertEqual(amenities.objects.count(), 0)
		