from django.urls import path
from . import views

urlpatterns = [
    path('listEmployee', views.employee_list),
    path('createEmployee', views.employee_create),
    path('updateEmployee/<int:pk>/', views.employee_update),
    path('deleteEmployee/<int:pk>/', views.employee_delete),
    path('listAddress', views.address_list),
    path('createAddress', views.address_create),
    path('updateAddress/<int:pk>/', views.address_update),
    path('deleteAddress/<int:pk>/', views.address_delete),
    path('login', views.formlogin),
    path('logout', views.logout_view),
]