from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LeaveManagement(models.Model):
    owner = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    leave_type = models.IntegerField()
    from_Date = models.DateField()
    to_Date = models.DateField()
    leave_applied_on = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)


class LeaveType(models.Model):
    key = models.AutoField(primary_key=True)
    leave_type = models.TextField(max_length=100)
    display_name = models.TextField(max_length=200)


class LeaveBalance(models.Model):
    owner = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    personal = models.IntegerField(default=10)
    casual = models.IntegerField(default=10)
    earned = models.IntegerField(default=10)
    sick = models.IntegerField(default=10)
    bereavement = models.IntegerField(default=5)
    optional = models.IntegerField(default=2)
    maternity = models.IntegerField(default=180)
    paternity = models.IntegerField(default=30)
