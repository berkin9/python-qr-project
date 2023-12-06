from rest_framework import permissions


# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsOwnPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.staff_user_list == request.user

