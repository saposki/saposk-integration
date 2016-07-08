
from django.conf.urls import url
from django.contrib import admin

from .views import(
    portrait,
    portrait_detail,
)

urlpatterns = [
    url(r'^$', portrait, name='port'),
    url(r'^(?P<id>\d+)/$', portrait_detail, name='detail'),
]
