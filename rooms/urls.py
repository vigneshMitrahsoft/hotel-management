from django.urls import path
from . import views

urlpatterns = [
	path('rooms', views.list_room),
	path('add_room', views.add_room),
	path('update_room/<int:id>', views.update_room),
	path('delete_room/<int:pk>',views.delete_room)
]