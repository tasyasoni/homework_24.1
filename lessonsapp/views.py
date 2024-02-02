from rest_framework import viewsets, generics
from lessonsapp.models import Course, Lesson, Subscription
from lessonsapp.paginators import LessonsPaginator
from lessonsapp.permissons import IsModerator, IsLessonOwner, IsCourseOwner
from lessonsapp.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, LessonIncludeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from lessonsapp.services import sendmail


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonsPaginator

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated | AllowAny]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsCourseOwner | IsModerator]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator | IsCourseOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsCourseOwner]
        return [permission() for permission in permission_classes]



class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | AllowAny]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | AllowAny, IsModerator | IsLessonOwner]
    pagination_class = LessonsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | AllowAny, IsModerator | IsLessonOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subscription = serializer.save(user=self.request.user)
        new_subscription.save()

class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsModerator | IsCourseOwner|AllowAny]

    def put(self, request, *args, **kwargs):
        sendmail.delay()
        return self.update(request, *args, **kwargs)

class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]