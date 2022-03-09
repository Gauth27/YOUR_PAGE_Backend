from ..models import *
from django.contrib.auth import authenticate

import requests


def loginUser(requestData):
    print("Request DATA: ", requestData)
    is_admin = False
    employeeID = ''
    user = authenticate(
        requestData, username=requestData['username'], password=requestData['password'])
    if user:
        print("User Object: ", user)
        #employeeID = user.employeeregistration.id
        if user.is_superuser:
            is_admin = True
        print("User is authenticated")
        res = requests.post(url='http://127.0.0.1:8000/token/',
                            data={
                                "username": f"{requestData['username']}",
                                "password": f"{requestData['password']}"
                            })
        token = res.json()
        print("Login Token:: ", token)
        return {'token': token['access'], 'is_admin': is_admin, 'employeeID': employeeID}
    else:
        print("Invalid Cred")
        raise Exception('Invalid Credentials')
