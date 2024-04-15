# In your_app/decorators.py
from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden

def group_required(group_name):
    """Decorator to restrict access to views based on group membership."""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                # Redirect or handle unauthorized access
                return HttpResponseForbidden("You don't have permission to access this page.")
        return _wrapped_view
    return decorator

def staff_required(view_func):
    """Decorator to restrict access to views to staff members."""
    return user_passes_test(lambda user: user.is_staff)(view_func)

def user_required(view_func):
    """Decorator to restrict access to views to regular users (non-staff)."""
    return user_passes_test(lambda user: not user.is_staff)(view_func)
