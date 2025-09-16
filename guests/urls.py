from django.contrib import admin  
from django.urls import path  
from guests import views  

urlpatterns = [
	path('listguests', views.guests_list),
	path('addguest', views.add_guest),
	path('updateguest/<int:pk>', views.update_guest),
	path('deleteguest/<int:pk>', views.delete_guest)
]