from django.urls import path
from . import views

urlpatterns = [
	path('requests', views.list_requests), 
	path('add_requests', views.add_requests),
	path('update_requests/<int:pk>', views.update_requests),
	path('delete_requests/<int:pk>', views.delete_requests)
]