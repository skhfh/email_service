from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^track/(?P<newsletter_id>\d+)/(?P<subscriber_id>\d+)/$',
        views.track_email_open,
        name='track_email_open')
]
