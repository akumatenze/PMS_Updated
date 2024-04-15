# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from OCI.CORE import admin
from .views import TenancyViewSet, RegionViewSet, ProfileViewSet, CompartmentViewSet

router = DefaultRouter()
router.register(r'tenancies', TenancyViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'compartments', CompartmentViewSet)

urlpatterns = [
    # Other URL patterns...
    path('admin/', admin.site.urls, name='admin_main'),
    # Other URL patterns...
]


from django.urls import path
from .views import dashboard, edit_dashboard, public_page, public_page_unrestricted

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('edit-dashboard/', edit_dashboard, name='edit_dashboard'),
    path('public-page/', public_page, name='public_page'),
    path('public-page-unrestricted/', public_page_unrestricted, name='public_page_unrestricted'),
    # Other URL patterns...
]

from django.urls import path
from . import views

urlpatterns = [
    # Customer URLs
    path('customers/', views.CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),

    # User URLs
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),

    # Project URLs
    path('projects/', views.ProjectListCreateAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailAPIView.as_view(), name='project-detail'),

    # Account URLs
    path('accounts/', views.AccountListCreateAPIView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', views.AccountDetailAPIView.as_view(), name='account-detail'),

    # Region URLs
    path('regions/', views.RegionListCreateAPIView.as_view(), name='region-list'),
    path('regions/<int:pk>/', views.RegionDetailAPIView.as_view(), name='region-detail'),

    # Tenancy URLs
    path('tenancies/', views.TenancyListCreateAPIView.as_view(), name='tenancy-list'),
    path('tenancies/<int:pk>/', views.TenancyDetailAPIView.as_view(), name='tenancy-detail'),

    # Profile URLs
    path('profiles/', views.ProfileListCreateAPIView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileDetailAPIView.as_view(), name='profile-detail'),

    # Compartment URLs
    path('compartments/', views.CompartmentListCreateAPIView.as_view(), name='compartment-list'),
    path('compartments/<int:pk>/', views.CompartmentDetailAPIView.as_view(), name='compartment-detail'),

    # KeyFile URLs
    path('keyfiles/', views.KeyFileListCreateAPIView.as_view(), name='keyfile-list'),
    path('keyfiles/<int:pk>/', views.KeyFileDetailAPIView.as_view(), name='keyfile-detail'),
]

