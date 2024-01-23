from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission
from usersapp.models import UserRoles



class IsModerator(BasePermission):
    pass

    # def has_permission(self, request, view):
    #     if request.user.role == UserRoles.MODERATOR:
    #         return True
    #     return False


class IsLessonOwner(BasePermission):
    pass

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner_lesson:
            return True
        return False


class IsCourseOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner_course:
            return True
        return False
