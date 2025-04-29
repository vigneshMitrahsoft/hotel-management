from django.contrib import admin  
from django.urls import path  
from users import views  

urlpatterns = [
	path('userslist', views.users_list),
	path('adduser', views.add_users),
	path('updateuser/<int:pk>', views.update_users),
	path('deleteuser/<int:pk>', views.delete_users)
]