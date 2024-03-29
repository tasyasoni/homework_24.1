# Generated by Django 5.0.1 on 2024-01-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status_paid',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус оплаты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_session',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='ID в Stripe'),
        ),
        migrations.AddField(
            model_name='payment',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Ссылка для оплаты'),
        ),
    ]
