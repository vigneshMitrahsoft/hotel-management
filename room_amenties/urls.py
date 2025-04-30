from django.urls import path
from . import views

urlpatterns = [
	path('room_amenties/create', views.create_room_amenties),
	path('room_amenties/update/<int:pk>', views.update_room_amenties)
]