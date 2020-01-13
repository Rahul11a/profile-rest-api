from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit there own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # Eg. if get request is made that falls under SAFE_METHODS hence it will accept the request.
        if request.method in permissions.SAFE_METHODS:
            return True

        return  obj.id == request.user.id
