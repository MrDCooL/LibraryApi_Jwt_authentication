from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsLibrarianOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 'librarian':
            return request.user.is_authenticated
        elif request.user.role == 'member' and request.method in SAFE_METHODS:
            return request.user.is_authenticated
        else:
            return False
        
class IsMember(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'member'