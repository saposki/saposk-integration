
from django.conf.urls import url
from django.contrib import admin

from .views import(
    crasher,
    crasher_detail,
)

urlpatterns = [
    url(r'^$', crasher, name='crash'),
    url(r'^(?P<id>\d+)/$', crasher_detail, name='detail'),
]
