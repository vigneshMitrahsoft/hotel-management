from django.urls import path
from . import views

urlpatterns = [
	path('amenties/create', views.create_amenity),
	path('amenties/list', views.list_amenties),
	path('amenties/update/<int:pk>', views.update_amenity),
	path('amenties/delete/<int:pk>', views.delete_amenity)
]