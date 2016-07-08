
from django.conf.urls import url
from django.contrib import admin

from .views import(
    street,
    street_detail
)

urlpatterns = [
    url(r'^$', street, name='st'),
    url(r'^(?P<id>\d+)/$', street_detail, name='detail'),
]
