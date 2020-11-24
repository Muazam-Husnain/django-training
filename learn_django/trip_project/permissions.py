from rest_framework import permissions
from .models import TripsUser


class IsSuperUserOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.trip_user
        if not user:
            return False
        return user.is_staff_member() or user.is_su_member()

