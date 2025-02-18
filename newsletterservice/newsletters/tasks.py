from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from newsletterservice.settings import DEFAULT_FROM_EMAIL, SITE_URL
from .models import Newsletter


@shared_task
def send_newsletter(newsletter_id):
    newsletter = Newsletter.objects.get(id=newsletter_id)
    subject = newsletter.subject
    content = newsletter.content
    recipients = newsletter.subscribers.all()
    mail_template_name = newsletter.template
    mail_template = 'newsletters/%s.html' % mail_template_name

    for recipient in recipients:
        tracking_url = SITE_URL + reverse(
            'track_email_open',
            kwargs={'newsletter_id': newsletter.id,
                    'subscriber_id': recipient.id}
        )
        html_message = render_to_string(mail_template, {
            'first_name': recipient.first_name,
            'last_name': recipient.last_name,
            'birth_date': recipient.birth_date.strftime('%d.%m'),
            'content': content,
            'tracking_url': tracking_url,
        })
        text_message = strip_tags(html_message)

        send_mail(
            subject,
            text_message,
            DEFAULT_FROM_EMAIL,
            [recipient.email],
            html_message=html_message
        )
