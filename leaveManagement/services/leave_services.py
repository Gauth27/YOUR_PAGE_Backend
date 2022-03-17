from ..models import LeaveManagement, LeaveType, HolidayList
from .serializers import LeaveTypeSerializer

from datetime import datetime
from datetime import timedelta


def leave_balance(user):
    balance = user.leavebalance_set.get(owner_id=user.id)
    return balance


def get_leaveType_from_DB(key):
    return LeaveType.objects.get(key=key)


def update_leave_Balance(user, leave_type, num):
    leave_type_from_DB = (
        LeaveTypeSerializer(get_leaveType_from_DB(leave_type), many=False).data
    )["leave_type"]
    print(leave_type_from_DB)

    balance_Of_LeaveType = leave_balance(user)
    if leave_type_from_DB == "personal":
        balance_Of_LeaveType.personal -= num
    elif leave_type_from_DB == "casual":
        balance_Of_LeaveType.casual -= num
    elif leave_type_from_DB == "earned":
        balance_Of_LeaveType.earned -= num
    elif leave_type_from_DB == "sick":
        balance_Of_LeaveType.sick -= num
    elif leave_type_from_DB == "bereavement":
        balance_Of_LeaveType.bereavement -= num
    elif leave_type_from_DB == "optional":
        balance_Of_LeaveType.optional -= num
    elif leave_type_from_DB == "maternity":
        balance_Of_LeaveType.maternity -= num
    elif leave_type_from_DB == "paternity":
        balance_Of_LeaveType.paternity -= num
    balance_Of_LeaveType.save()


def get_HolidayList():
    hol_list = HolidayList.objects.all()
    date_list  = [i.date.strftime('%Y-%m-%d') for i in hol_list]
    print(date_list)
    return date_list


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


def leave_management(request_data, user):
    new_leave = LeaveManagement.objects.create(
        owner=user,
        leave_type=request_data["leave_type"],
        from_Date=request_data["from_Date"],
        to_Date=request_data["to_Date"],
    )
    #TODO Refactor the code for better Readability.
    date_format = "%Y-%m-%d"
    from_date = datetime.strptime(request_data["from_Date"], date_format)
    to_date = datetime.strptime(request_data["to_Date"], date_format)
    num_Of_Days = (to_date - from_date).days + 1
    weekends = [5, 6]
    holiday_List = get_HolidayList() # Fetches the list of Holidays from the DB.
    for dt in daterange(from_date, to_date):
        if dt.strftime('%Y-%m-%d') in holiday_List:
            num_Of_Days -= 1     
        elif dt.weekday() in weekends:
            num_Of_Days -= 1

    new_leave.save() # Creates a new entry in the Leave Mangement Table
    update_leave_Balance(user, request_data["leave_type"], num_Of_Days) # Updates the Leave Balance Table.
