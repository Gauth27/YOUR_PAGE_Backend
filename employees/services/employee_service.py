from operator import le
from django.contrib.auth.models import User
from ..models import EmployeeRegistration
from leaveManagement.models import LeaveBalance, LeaveManagement


def registerEmployeeData(data):
    new_User = User.objects.create(
        email = data['email'],
        username = data['email'],
        is_staff = data['flexSwitchCheckChecked'] == 'true',
    )
    new_User.save()
    
    last_User = User.objects.last()
    last_User.set_password('123456')
    last_User.save()

    new_Employee = EmployeeRegistration.objects.create(
        owner=last_User,
        name=data['name'],
        gender=data['gender'],
        dateOfBirth=data['dateOfBirth'],
        highest_Qualification=data['highest_Qualification'],
        pan=data['pan'],
        aadhar=data['aadhar'],
        email=data['email'],
        personal_email=data['personal_email'],
        blood_group=data['blood_group'],
        address=data['address'],
        phone_number=data['phone_number'],
        emergency_contact_number=data['emergency_contact_number'],
        nationality=data['nationality'],
        state=data['state'],
        city=data['city'],
        pin_code=data['pin_code'],
        department=data['department'],
        reporting=data['reporting'],
        grade=data['grade'],
        designation=data['designation'],
        bank_account=data['bank_account'],
        joining_date=data['joining_date'],
        last_working_date=data['last_working_date'],
        _photo = data['photo_image'],
        # documents = data['documents'],
    )
    new_Employee.save()

    leave_balance = LeaveBalance.objects.create(
        owner = last_User
    )
    leave_balance.save()


def getEmployeeByID(id):
    return EmployeeRegistration.objects.get(id=id)


def getAllEmployees():
    employees = EmployeeRegistration.objects.all()
    return employees