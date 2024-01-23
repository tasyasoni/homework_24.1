from django.urls import path
from lessonsapp.apps import LessonsappConfig
from rest_framework.routers import DefaultRouter

from lessonsapp.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionUpdateView, SubscriptionDestroyAPIView

app_name = LessonsappConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_one'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('course/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('course/update_sub/<int:pk>/', SubscriptionUpdateView.as_view(), name='subscription_update'),
    path('course/delete_sub/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

] + router.urls