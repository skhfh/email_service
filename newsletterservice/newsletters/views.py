# coding=utf-8

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import NewsletterForm
from .models import EmailOpen, Newsletter, Subscriber
from .tasks import send_newsletter

GIF_PIXEL = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
    b'\xff\xff\xff\x21\xf9\x04\x01\x0a\x00\x00\x00\x2c\x00\x00\x00\x00'
    b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
)


def index(request):
    """Главная с формой для отправки/планировании рассылки"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            send_later = form.cleaned_data.get('send_later')
            newsletter.date = send_later or timezone.now()
            newsletter.save()
            form.save_m2m()

            if send_later:
                send_newsletter.apply_async((newsletter.id,), eta=send_later)
                return JsonResponse({'message': 'Рассылка запланирована!'},
                                    status=200)
            else:
                send_newsletter.delay(newsletter.id)
                return JsonResponse({'message': 'Рассылка отправлена!'},
                                    status=200)
        else:
            return JsonResponse({'error': 'Ошибка в данных формы!'},
                                status=400)
    else:
        form = NewsletterForm()
    return render(request, 'index.html', {'form': form})


def track_email_open(request, subscriber_id, newsletter_id):
    """Записывает факт открытия письма"""
    if subscriber_id and newsletter_id:
        subscriber = get_object_or_404(Subscriber, id=subscriber_id)
        newsletter = get_object_or_404(Newsletter, id=newsletter_id)
        EmailOpen.objects.get_or_create(subscriber=subscriber,
                                        newsletter=newsletter)
    return HttpResponse(GIF_PIXEL, content_type='image/gif')
