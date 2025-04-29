from django.urls import path
from . import views

urlpatterns = [
	path('room_type', views.list_room_type), 
	path('add_room_type', views.add_room_type),
	path('update_room_type/<int:pk>', views.update_room_type),
	path('delete_room_type/<int:pk>', views.delete_room_type)
]