from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.room_list),
    path('addroom', views.addroom),
    path('update/<int:id>', views.updateroom),
    path('delete/<int:pk>',views.deleteroom), 
]
