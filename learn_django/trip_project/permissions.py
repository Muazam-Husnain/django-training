from rest_framework import permissions
from .models import TripsUser


class IsSuperUserOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        user = TripsUser.objects.get(pk=user.id)
        return user.is_staff_member() or user.is_su_member()

