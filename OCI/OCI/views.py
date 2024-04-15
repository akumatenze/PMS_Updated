# views.py

from django.views.generic import TemplateView

class AdminView(TemplateView):
    template_name = 'admin.html'

class StaffView(TemplateView):
    template_name = 'staff.html'

class UsersView(TemplateView):
    template_name = 'users.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class LogoutView(TemplateView):
    template_name = 'logout.html'

class SignupView(TemplateView):
    template_name = 'signup.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'
