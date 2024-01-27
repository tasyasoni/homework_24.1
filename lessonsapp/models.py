from django.db import models
from usersapp.models import NULLABLE, User


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    video = models.TextField(max_length=100, verbose_name='ссылка_видео', **NULLABLE)
    owner_lesson = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец_урока')
    price = models.CharField(default=100, **NULLABLE, verbose_name='стоимость_урока')
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='описание', **NULLABLE)
    lessons = models.ManyToManyField(Lesson, verbose_name='уроки')
    owner_course = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец_курса')
    price = models.CharField(default=100, **NULLABLE, verbose_name='стоимость_курса')
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscription', verbose_name='курс')
    subscribed = models.BooleanField(default=False, verbose_name='статус_подписки')

    def __str__(self):
        return f"{self.user}: {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
