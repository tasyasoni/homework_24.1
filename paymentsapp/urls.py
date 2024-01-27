from django.urls import path
from paymentsapp.apps import PaymentsappConfig
from paymentsapp.views import PaymentListAPIView, PaymentRetrieveAPIView,\
    PaymentCourseCreateAPIView, PaymentLessonCreateAPIView

app_name = PaymentsappConfig.name


urlpatterns = [
    # path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
    # path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_one'),
    # path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    # path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),
    path('course/<int:pk>/create/', PaymentCourseCreateAPIView.as_view(), name='course_payment'),
    path('lesson/<int:pk>/create/', PaymentLessonCreateAPIView.as_view(), name='lesson_payment'),
    path('course/<int:pk>/retrieve/', PaymentRetrieveAPIView.as_view(), name='course_retrieve'),
    path('lesson/<int:pk>/retrieve/', PaymentRetrieveAPIView.as_view(), name='lesson_retrieve'),
]