from django.contrib import admin  
from django.urls import path  
from hotel import views  

urlpatterns = [
	path('hotellist', views.hotel_list),
	path('addhotel', views.add_hotel),
    path('updatehotel/<int:pk>', views.update_hotel),
    path('deletehotel/<int:pk>', views.delete_hotel)
]