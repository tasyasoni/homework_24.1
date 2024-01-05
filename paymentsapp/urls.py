from django.urls import path
from paymentsapp.apps import PaymentsappConfig
from paymentsapp.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
    PaymentDestroyAPIView

app_name = PaymentsappConfig.name


urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_one'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),
]