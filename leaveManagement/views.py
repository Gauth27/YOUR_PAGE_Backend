from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .services.serializers import LeaveBalanceSerializer, ApplyLeaveSerializer
from .services.leave_services import *
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_leave_balance(request):
    user =  request.user
    print(user)
    return Response(LeaveBalanceSerializer(leave_balance(user), many=False).data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def apply_leave(request):
    user =  request.user
    return Response(ApplyLeaveSerializer(leave_management(request.data, user), many=False).data)