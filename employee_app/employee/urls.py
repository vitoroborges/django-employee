from django.urls import path
from . import views

urlpatterns = [
    path('listEmployee', views.employee_list, name='employee_list'),
    path('createEmployee', views.employee_create, name='employee_create'),
    path('updateEmployee/<int:pk>/', views.employee_update, name='employee_update'),
    path('deleteEmployee/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('login', views.formlogin, name='login'),
    path('logout', views.logout_view, name='logout'),
]