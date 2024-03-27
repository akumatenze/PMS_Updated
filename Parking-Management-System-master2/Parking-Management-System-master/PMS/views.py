from django.shortcuts import render

from PMS.serializers import BuildingSerializers, RowsSerializers, FloorSerializers, ColoumnSerializers,VehicleSerializers
from .models import Building, Rows, Floor, Coloumn, Vehicle
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated

# Custom permission class for admin-only access
class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to create, update or delete objects.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the admin user.
        return request.user and request.user.is_admin


# Create your views here.

class BuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers
    permission_classes = [IsAdminUser]  # Set permissions for this view


class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializers
    permission_classes = [IsAdminOrReadOnly]  # Set permissions for this view


class RowsView(generics.ListCreateAPIView):
    queryset = Rows.objects.all()
    serializer_class = RowsSerializers
    permission_classes = [IsAdminOrReadOnly]  # Set permissions for this view


class ColoumnView(generics.ListCreateAPIView):
    queryset = Coloumn.objects.all()
    serializer_class = ColoumnSerializers
    permission_classes = [IsAdminOrReadOnly]  # Set permissions for this view


class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers
    permission_classes = [IsAdminOrReadOnly]  # Set permissions for this view


def dashboard(request):
    # Get counts of users with different roles
    admin_count = User.objects.filter(is_superuser=True).count()
    staff_count = User.objects.filter(is_staff=True, is_superuser=False).count()
    user_count = User.objects.filter(is_staff=False, is_superuser=False).count()

    context = {
        'admin_count': admin_count,
        'staff_count': staff_count,
        'user_count': user_count,
    }

    return render(request, 'dashboard.html', context)

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .permission import IsAuthenticatedAndAdmin

class ExampleAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def get(self, request):
        return Response("This is an example API view")
