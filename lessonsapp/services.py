from datetime import timezone

from celery import shared_task
from django.core.mail import send_mail
from config import settings
from usersapp.models import User


@shared_task
def sendmail():
    send_mail(
        'Подписка на обновления курса',
        'На вашем курсе обновлены обучающие материалы.',
        settings.EMAIL_HOST_USER,
        ['TasyaSoni@yandex.ru'],
        fail_silently=False,
    )

@shared_task
def block_inactive_users():
    inactive_users = User.objects.filter(last_login__lt = timezone.now() - timezone.timedelta(days=30), is_active=True)
    inactive_users.update(is_active=False)
    inactive_users.save()
