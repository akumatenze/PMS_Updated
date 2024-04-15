"""
URL configuration for OCI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

#from OCI.CORE import views
#from django.models import views

app_name = 'OCI'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_app_specific'),
    path('staff/', admin.site.urls),
    path('users/', admin.site.urls),
    path('login/', admin.site.urls),
    path('logout/', admin.site.urls),
    path('signup/', admin.site.urls),
    path('profile/', admin.site.urls),
]