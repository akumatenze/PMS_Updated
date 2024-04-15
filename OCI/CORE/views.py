# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Tenancy, Region, Profile, Compartment
from .serializers import TenancySerializer, RegionSerializer, ProfileSerializer, CompartmentSerializer
from guardian.decorators import permission_required as guardian_permission_required # type: ignore

# API Views
class TenancyViewSet(viewsets.ModelViewSet):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CompartmentViewSet(viewsets.ModelViewSet):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

# Custom Views
@login_required
@permission_required('oci.view_dashboard', raise_exception=True)
def dashboard(request):
    # This view requires the user to be logged in and have the 'view_dashboard' permission
    return render(request, 'oci/dashboard.html')

@login_required
@permission_required('oci.edit_dashboard', raise_exception=True)
def edit_dashboard(request):
    # This view requires the user to be logged in and have the 'edit_dashboard' permission
    return render(request, 'oci/edit_dashboard.html')

@login_required
def public_page(request):
    # This view is accessible to all logged-in users
    return render(request, 'oci/public_page.html')

def public_page_unrestricted(request):
    # This view is accessible to all users, even if they're not logged in
    return render(request, 'oci/public_page_unrestricted.html')

# Additional Custom Views
@login_required
@guardian_permission_required('core.view_tenancy', return_403=True)
def my_view(request):
    # View logic...
    return render(request, 'my_view.html', {})

# You can add more custom views here...

# Views from previous code
@login_required
def my_protected_view(request):
    # View logic...
    return render(request, 'my_protected_view.html', {})

@staff_required # type: ignore
def staff_only_view(request):
    # View logic...
    return render(request, 'staff_only_view.html', {})

@user_required # type: ignore
def user_only_view(request):
    # View logic...
    return render(request, 'user_only_view.html', {})

class CustomPasswordChangeView(PasswordChangeView): # type: ignore
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'

class CustomLoginView(LoginView): # type: ignore
    form_class = AuthenticationForm # type: ignore
    template_name = 'registration/login.html'

@permission_required('access_staff_content', raise_exception=True)
def staff_only_view(request):
    return HttpResponse('This is a staff-only view')

@permission_required('access_user_content', raise_exception=True)
def user_only_view(request):
    return HttpResponse('This is a user-only view')

def both_permissions_view(request):
    if request.user.has_perms(['access_staff_content', 'access_user_content']):
        return HttpResponse('This view requires both staff and user permissions')
    elif request.user.has_perm('access_staff_content'):
        return HttpResponse('This view requires only staff permission')
    elif request.user.has_perm('access_user_content'):
        return HttpResponse('This view requires only user permission')
    else:
        return HttpResponse('You do not have permission to access this view')


# OCI/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product

def index(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'customers': customers, 'products': products})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def purchase(request, product_id):
    # Logic to handle a purchase, e.g., updating inventory, creating an order, etc.
    product = Product.objects.get(pk=product_id)
    return HttpResponse(f"Thank you for purchasing {product.name}!")

from django.shortcuts import render
from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Customer, User, Project, Account, Region, Tenancy, Profile, Compartment, KeyFile
from .serializers import CustomerSerializer, UserSerializer, ProjectSerializer, AccountSerializer, RegionSerializer, TenancySerializer, ProfileSerializer, CompartmentSerializer, KeyFileSerializer

# Customer views
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# User views
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Project views
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Account views
class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Region views
class RegionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# Tenancy views
class TenancyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

class TenancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

# Profile views
class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Compartment views
class CompartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

class CompartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

# KeyFile views
class KeyFileListCreateAPIView(generics.ListCreateAPIView):
    queryset = KeyFile.objects.all()
    serializer_class = KeyFileSerializer

class KeyFileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyFile.objects.all()
    serializer_class = KeyFileSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Customer, User, Project, Account, Region, Tenancy, Profile, Compartment, KeyFile
from .serializers import CustomerSerializer, UserSerializer, ProjectSerializer, AccountSerializer, RegionSerializer, TenancySerializer, ProfileSerializer, CompartmentSerializer, KeyFileSerializer

# Customer views
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# User views
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Project views
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Account views
class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Region views
class RegionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# Tenancy views
class TenancyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

class TenancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

# Profile views
class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Compartment views
class CompartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

class CompartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

# KeyFile views
class KeyFileListCreateAPIView(generics.ListCreateAPIView):
    queryset = KeyFile.objects.all()
    serializer_class = KeyFileSerializer

class KeyFileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyFile.objects.all()
    serializer_class = KeyFileSerializer

# views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Customer, User, Project, Account, Region, Tenancy, Profile, Compartment, KeyFile
from .serializers import CustomerSerializer, UserSerializer, ProjectSerializer, AccountSerializer, RegionSerializer, TenancySerializer, ProfileSerializer, CompartmentSerializer, KeyFileSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add token authentication

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add token authentication

# Other views with similar changes

from rest_framework import viewsets
from .models import Tenancy, Region, Profile, Compartment
from .serializers import TenancySerializer, RegionSerializer, ProfileSerializer, CompartmentSerializer

class TenancyViewSet(viewsets.ModelViewSet):
    queryset = Tenancy.objects.all()
    serializer_class = TenancySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CompartmentViewSet(viewsets.ModelViewSet):
    queryset = Compartment.objects.all()
    serializer_class = CompartmentSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oci import config

@login_required
def dashboard(request):
    # Retrieve user-specific OCI credentials and configuration
    user = request.user
    oci_user_credentials = user.oci_credentials
    oci_config = {
        'user': oci_user_credentials['user'],
        'key_file': oci_user_credentials['key_file'],
        'fingerprint': oci_user_credentials['fingerprint'],
        'tenancy': oci_user_credentials['tenancy'],
        'region': oci_user_credentials['region']
        # Add other OCI configuration parameters as needed
    }
    
    # Configure OCI SDK with the user's session-based configuration
    config.from_dict(oci_config)

    # Now you can use the OCI SDK to interact with OCI services
    # For example:
    # oci.identity.IdentityClient(...)

    return render(request, 'dashboard.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oci import config

@login_required
def dashboard(request):
    # Retrieve user-specific OCI credentials and configuration
    user = request.user
    oci_user_credentials = user.oci_credentials
    oci_config = {
        'user': oci_user_credentials['user'],
        'key_file': oci_user_credentials['key_file'],
        'fingerprint': oci_user_credentials['fingerprint'],
        'tenancy': oci_user_credentials['tenancy'],
        'region': oci_user_credentials['region']
        # Add other OCI configuration parameters as needed
    }
    
    # Configure OCI SDK with the user's session-based configuration
    config.from_dict(oci_config)

    # Now you can use the OCI SDK to interact with OCI services
    # For example:
    # oci.identity.IdentityClient(...)

    return render(request, 'dashboard.html')
