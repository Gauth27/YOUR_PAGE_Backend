from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# Create your views here.

from .services.employee_service import *
from .services.serializers import *
from .services.auth_service import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def homePage(request):
    return Response(EmployeeNameSerializer(getAllEmployees(), many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employeeDetails(request, pk):
    return Response(EmployeeSerializer(getEmployeeByID(pk), many=False).data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def employeeRegisration(request):
    # return Response(EmployeeSerializer(registerEmployeeData(request.data), many=False).data)
    return Response(registerEmployeeData(request.data))


@permission_classes([IsAdminUser])
class ApiEmployeesListView(ListAPIView):
    # queryset = EmployeeRegistration.objects.all()
    queryset = EmployeeRegistration.objects.filter(is_deleted = False)
    serializer_class = EmployeeNameSerializer
    pagination_class = PageNumberPagination 


@api_view(['POST'])
def login(request):
    # print('TEST: ', request.data)
    return Response(loginUser(request.data))


@api_view(['GET'])
@permission_classes([IsAdminUser])
def employeeSearch(request):
    return Response(EmployeeNameSerializer(getEmployeeBySearch(request.GET['name']), many=True).data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteEmployee(request, pk):
    return Response(deleteEmployeeByID(pk))


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateEmployeeDetails(request, pk):
    # return Response(EmployeeSerializer(updateEmployee(pk, request.data), many=False).data)
    return Response(updateEmployee(pk, request.data))