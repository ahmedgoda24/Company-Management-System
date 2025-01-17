# from rest_framework import permissions

# class IsAdminUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role == 'ADMIN'

# class IsManager(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role == 'MANAGER'
    

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'


class IsManager(BasePermission):
    """
    Allows access to managers and admins.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['MANAGER', 'ADMIN']


class IsEmployee(BasePermission):
    """
    Allows access to employees, managers, and admins.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['EMPLOYEE', 'MANAGER', 'ADMIN']

    

