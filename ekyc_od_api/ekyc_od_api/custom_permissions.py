from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
    
class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user

class IsSuperUserOrStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
    
class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        return not (request.user.is_superuser or request.user.is_staff)