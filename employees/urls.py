from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home-page', views.homePage),
    path('login-page', views.login),
    path('list', views.ApiEmployeesListView.as_view()),
    path('details/<str:pk>', views.employeeDetails),
    path('employee-registration', views.employeeRegisration),
    path('employee-search', views.employeeSearch),
    path('delete-employee/<str:pk>', views.deleteEmployee),
    path('edit-employee/<str:pk>', views.updateEmployeeDetails),
]