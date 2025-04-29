from django.urls import path
from . import views

urlpatterns = [
    path('staffs/create', views.create_staff),
    path('staffs/list/',views.list_staff),
    path('staffs/<int:pk>/', views.get_staff),
    path('staffs/update/<int:pk>/', views.update_staff),
    path('staffs/delete/<int:pk>/', views. delete_staff),
]


