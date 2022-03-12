from django.urls import path
from .import views

urlpatterns = [
    path('balance', views.display_leave_balance),
    path('apply-leave', views.apply_leave),
]