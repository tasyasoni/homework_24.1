from django.conf import settings
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
        print(new_payment)
        new_payment.user = self.request.user
        print(new_payment.user)
        course_pk = self.kwargs.get('pk')
        print(course_pk)
        new_payment.course = Course.objects.get(pk=course_pk)
        print(new_payment.course)
        session = StripePayments(settings.STRIPE_API_KEY).create_session(new_payment.course, new_payment.user)
        new_payment.stripe_session = session.id
        print(new_payment.stripe_session)
        new_payment.url = session.url
        print(new_payment.url)
        new_payment.save()


class PaymentLessonCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        new_payment = serializer.save()
        print(new_payment)
        new_payment.user = self.request.user
        print(new_payment.user)
        lesson_pk = self.kwargs.get('pk')
        print(lesson_pk)
        new_payment.lesson = Lesson.objects.get(pk=lesson_pk)
        print(new_payment.lesson)
        session = StripePayments(settings.STRIPE_API_KEY).create_session(new_payment.lesson, new_payment.user)
        new_payment.stripe_session = session.id
        print(new_payment.stripe_session)
        new_payment.url = session.url
        print(new_payment.url)
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