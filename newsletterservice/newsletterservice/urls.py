from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('newsletters.urls')),
    url(r'^admin/', admin.site.urls),
]
