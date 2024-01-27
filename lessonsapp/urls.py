from django.urls import path
from config.urls import schema_view
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



    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls