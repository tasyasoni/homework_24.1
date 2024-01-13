from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE )
    avatar = models.ImageField(upload_to='user/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



    def __str__(self):
        return  f'{self.email}'


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
