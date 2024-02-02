from celery import shared_task
from django.core.mail import send_mail
from config import settings


def sendmail():
    send_mail(
        'Подписка на обновления курса',
        'На вашем курсе обновлены обучающие материалы.',
        settings.EMAIL_HOST_USER,
        ['TasyaSoni@yandex.ru'],
        fail_silently=False,
    )