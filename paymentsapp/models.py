from django.db import models

from lessonsapp.models import Course, Lesson
from usersapp.models import User, NULLABLE


class Payment(models.Model):

    PERIODICITY_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date = models.DateField(verbose_name="дата оплаты")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="оплаченный курс")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name="оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма оплаты")
    payment_method = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name="способ оплаты")
    stripe_session = models.CharField(max_length=500, **NULLABLE, verbose_name='ID в Stripe')
    status_paid = models.CharField(max_length=100, **NULLABLE, verbose_name='Статус оплаты')
    url = models.URLField(verbose_name='Ссылка для оплаты', **NULLABLE, max_length=500)

    def __str__(self):
        return f'{self.user} - {self.date} - {self.amount}'

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"