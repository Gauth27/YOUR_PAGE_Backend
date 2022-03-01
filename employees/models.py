from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeRegistration(models.Model):
    owner = models.OneToOneField(to=User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    gender = models.CharField(max_length=10, blank=False, null=False)
    dateOfBirth = models.CharField(max_length=10, blank=False, null=False)
    highest_Qualification = models.CharField(max_length=200, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=False, null=False)
    aadhar = models.CharField(max_length=12,blank=False, null=False)
    passport = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    personal_email = models.EmailField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=500, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    emergency_contact_number = models.IntegerField(blank=False, null=False)
    nationality = models.TextField(max_length=50, null=False, blank=False)
    state = models.TextField(max_length=50, null=False, blank=False)
    city = models.TextField(max_length=50, null=False, blank=False)
    pin_code = models.IntegerField(blank=False, null=False)
    department = models.CharField(max_length=50, blank=True, null=True)
    reporting = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    photo_image = models.CharField(max_length=500, blank=True, null=True)
    documents = models.CharField(max_length=500, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    joining_date = models.CharField(max_length=10, blank=True, null=True)
    last_working_date = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.name