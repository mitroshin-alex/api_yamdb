from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == 'admin')


class OwnPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.username == obj.username

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
