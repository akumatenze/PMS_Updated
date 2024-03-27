from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAuthenticatedAndAdmin(BasePermission):
    """
    Custom permission class that requires the user to be authenticated and an admin.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is an admin
        print(request.user.role)
        if request.user.role == 2:
            return True
        
        return False
