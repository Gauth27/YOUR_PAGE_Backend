from django.contrib import admin
from .models import LeaveManagement, LeaveBalance, LeaveType

# Register your models here.
admin.register(LeaveManagement)
admin.register(LeaveBalance)
admin.register(LeaveType)
