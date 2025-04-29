from django.urls import path
from . import views

urlpatterns = [
	path('Api/rooms', views.list_room),
	path('Api/add_room', views.add_room),
	path('Api/update_room/<int:id>', views.update_room),
	path('Api/delete_room/<int:pk>',views.delete_room)
]
