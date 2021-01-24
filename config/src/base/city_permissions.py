from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class CitizenPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class BusinessOwnerPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class MayorPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_mayor)


class GovernorPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_governor)
