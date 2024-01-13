from django.db import models
from usersapp.models import NULLABLE, User


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    video = models.TextField(max_length=100, verbose_name='ссылка_видео')
    owner_lesson = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец_урока')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='описание')
    lessons = models.ManyToManyField(Lesson, verbose_name='уроки')
    owner_course = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец_курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'



