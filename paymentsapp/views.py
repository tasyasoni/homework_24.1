from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessonsapp.models import Course, Lesson
from paymentsapp.models import Payment
from paymentsapp.serializers import PaymentSerializer
from paymentsapp.services import StripePayments


class PaymentCourseCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.paid_course = Course.objects.get(pk=self.kwargs.get('pk'))
        new_payment.save()
        price = new_payment.paid_course.price
        stripe_payment = StripePayments(user=new_payment.user, course=new_payment.paid_course, amount=price)
        new_payment.stripe_session = stripe_payment.create_session()['session_id']
        new_payment.url = stripe_payment.create_session()['url_pay']
        new_payment.save()


class PaymentLessonCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.paid_lesson = Lesson.objects.get(pk=self.kwargs.get('pk'))
        new_payment.save()
        price = new_payment.paid_lesson.price
        stripe_payment = StripePayments(user=new_payment.user, course=new_payment.paid_lesson, amount=price)
        new_payment.stripe_session = stripe_payment.create_session()['session_id']
        new_payment.url = stripe_payment.create_session()['url_pay']
        new_payment.save()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ['date']


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get(self, request, *args, **kwargs):
        payment = self.queryset.get(pk=self.kwargs.get('pk'))
        session_id = payment.stripe_session
        status_paid = StripePayments.retrieve_session(session_id=session_id)
        payment.status_paid = status_paid
        payment.save()
        return Response({'status': payment.status_paid}, )

class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()