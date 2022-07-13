from rest_framework import permissions


class IsPremiumClient(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_premium_client)
