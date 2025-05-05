from django.urls import path
from . import views

urlpatterns = [
	path('create_staff/', views.create_staff),
	path('list_staff/',views.list_staff),
	path('staff/<int:pk>/', views.get_staff),
	path('update_staff/<int:pk>/', views.update_staff),
	path('delete_staff/<int:pk>/', views. delete_staff),
]