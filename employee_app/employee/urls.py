from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'employees', EmployeeViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('listEmployee', views.employee_list),
    path('createEmployee', views.employee_create),
    path('updateEmployee/<int:pk>/', views.employee_update),
    path('deleteEmployee/<int:pk>/', views.employee_delete),
    path('login', views.formlogin),
    path('logout', views.logout_view),
]

urlpatterns += router.urls
urlpatterns += [
    path('api/', include(router.urls)),
]