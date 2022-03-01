from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from django.contrib.auth.models import User
from ..models import EmployeeRegistration


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRegistration
        fields = '__all__'

class EmployeeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRegistration
        fields = ['name', 'id']