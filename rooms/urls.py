from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.room_list),
    path('addroom', views.add_room),
    path('update/<int:id>', views.update_room),
    path('delete/<int:pk>',views.delete_room), 
]
