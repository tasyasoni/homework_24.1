from rest_framework.permissions import BasePermission
from usersapp.models import UserRoles



class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsLessonOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.lesson_owner:
            return True
        return False


class IsCourseOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.course_owner:
            return True
        return False
