# coding=utf-8
from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    """Модель подписчиков"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __unicode__(self):
        return u'%s %s - %s' % (self.first_name, self.last_name, self.email)


class Newsletter(models.Model):
    """Модель рассылок"""
    subject = models.CharField(max_length=100)
    content = models.TextField()
    subscribers = models.ManyToManyField(Subscriber,
                                         related_name='newsletter')
    template = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        choices=[
            ('birthdayletter', 'Письмо с Днем Рождения'),
            ('infoletter', 'Информационное письмо'),
        ])
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __unicode__(self):
        return u'%s' % self.subject


class EmailOpen(models.Model):
    """Модель факта открытия писем"""
    subscriber = models.ForeignKey(Subscriber,
                                   on_delete=models.CASCADE,
                                   related_name='open_email')
    newsletter = models.ForeignKey(Newsletter,
                                   on_delete=models.CASCADE,
                                   related_name='open_email')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Факт открытия сообщения'
        verbose_name_plural = 'Факты открытия сообщения'

    def __unicode__(self):
        return u'%s - %s' % (self.subscriber.email, self.newsletter.subject)
