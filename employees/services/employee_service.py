from operator import le
from django.contrib.auth.models import User
from django.db.models import Q
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
        photo_image = data['photo_image'],
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
    # employees = EmployeeRegistration.objects.all()
    employees = EmployeeRegistration.objects.filter(is_deleted = False)
    return employees


def getEmployeeBySearch(name):
    search_query = ''
    if name:
        search_query = name
    print('search_query', search_query)
    # employees = EmployeeRegistration.objects.distinct().filter(
    #     Q(title__icontains=search_query)|
    #     Q(description__icontains=search_query)|
    #     Q(owner__name__icontains=search_query)|
    #     Q(tags__in=tags)
    # )
    employees = EmployeeRegistration.objects.filter(name__icontains=search_query)
    return employees


def deleteEmployeeByID(id):
    employee = EmployeeRegistration.objects.get(id=id)
    # employee.delete()
    employee.is_deleted = True
    employee.save()
    return "IS_DELETE attribute is set to True in the Database"


def updateEmployee(id, data):
    employee = EmployeeRegistration.objects.get(id=id)
    owner = employee.owner

    owner.email = data['email']
    owner.username = data['email']
    print("IS ADMIN: ", data['flexSwitchCheckChecked'] == 'true',)
    owner.is_staff = data['flexSwitchCheckChecked'] == 'true'
    owner.save()

    print("OWNER: ", owner.email)
    employee.name = data['name']
    employee.gender=data['gender']
    employee.dateOfBirth=data['dateOfBirth']
    employee.highest_Qualification=data['highest_Qualification']
    employee.pan=data['pan']
    employee.aadhar=data['aadhar']
    employee.email=data['email']
    employee.personal_email=data['personal_email']
    employee.blood_group=data['blood_group']
    employee.address=data['address']
    employee.phone_number=data['phone_number']
    employee.emergency_contact_number=data['emergency_contact_number']
    employee.nationality=data['nationality']
    employee.state=data['state']
    employee.city=data['city']
    employee.pin_code=data['pin_code']
    employee.department=data['department']
    employee.reporting=data['reporting']
    employee.grade=data['grade']
    employee.designation=data['designation']
    employee.bank_account=data['bank_account']
    employee.joining_date=data['joining_date']
    employee.last_working_date=data['last_working_date']
    employee.photo_image = data['photo_image']
    employee.save()

    return "Employee Details Succesfully Updated"