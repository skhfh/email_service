# coding=utf-8
from django import forms

from .models import Newsletter, Subscriber


class NewsletterForm(forms.ModelForm):
    """Форма для Рассылки"""
    template = forms.ChoiceField(
        required=True,
        label='Шаблон письма',
        choices=[
            ('infoletter', 'Информационное письмо'),
            ('birthdayletter', 'Письмо с Днем Рождения'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    subscribers = forms.ModelMultipleChoiceField(
        queryset=Subscriber.objects.all(),
        required=True,
        label='Список подписчиков',
    )
    send_later = forms.DateTimeField(
        required=False,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local',
                                          'class': 'form-control'}),
        label="Выберите дату и время для отправки"
    )

    class Meta:
        model = Newsletter
        fields = ('subject',
                  'content',
                  'template',
                  'subscribers',
                  'send_later')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'rows': '3'}),
        }
        labels = {
            'subject': 'Тема рассылки',
            'content': 'Содержание рассылки',
        }
