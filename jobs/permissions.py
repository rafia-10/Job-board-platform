from rest_framework import permissions      

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """    Only allow admins to POST/PUT/DELETE. Users can GET. """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'