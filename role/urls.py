from django.urls import path
from . import views

urlpatterns = [
    path('role/create', views.create_role),
    path('role/list', views.list_roles),
    path('role/update/<int:pk>', views.update_role),
    path('role/delete/<int:pk>', views.delete_role)
]