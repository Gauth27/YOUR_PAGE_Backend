
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class LeaveManagement(models.Model):
#     owner = models.ForeignKey(to=User, null=True, blank=True)
#     leave_type = models.IntegerField(max_length=2)
#     from_Date = models.DateField()
#     to_Date = models.DateField()
#     leave_applied_on = models.DateTimeField(auto_now_add=True)
#     id = models.AutoField(primary_key=True)


# class LeaveType(models.Model):
#     key = models.AutoField(primary_key=True)
#     values = models.TextField(max_length=100)
#     display_name = models.TextField(max_length=200)


# class LeaveBalance(models.Model):
#     owner = models.ForeignKey(to=User, null=True, blank=True)
#     personal = models.IntegerField(max_length=3, default=10)
#     casual = models.IntegerField(max_length=3, default=10)
#     earned = models.IntegerField(max_length=3, default=10)
#     sick = models.IntegerField(max_length=3, default=10)
#     bereavement = models.IntegerField(max_length=3, default=5)
#     optional = models.IntegerField(max_length=3, default=2)
#     maternity = models.IntegerField(max_length=3, default=180)
#     paternity = models.IntegerField(max_length=3, default=30)