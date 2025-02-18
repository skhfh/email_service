# coding=utf-8
from django.contrib import admin

from .models import EmailOpen, Newsletter, Subscriber


class EmailOpenAdmin(admin.ModelAdmin):
    """Добавление в админку управление проверки открытия писем"""
    list_display = ('subscriber', 'newsletter', 'date')


class NewsletterAdmin(admin.ModelAdmin):
    """Добавление в админку управление рассылками"""
    list_display = ('pk', 'subject', 'content')
    search_fields = ('subject',)


class SubscriberAdmin(admin.ModelAdmin):
    """Добавление в админку управление подписчиками"""
    list_display = ('pk', 'first_name', 'last_name', 'email', 'birth_date')
    search_fields = ('email',)


admin.site.register(EmailOpen, EmailOpenAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
