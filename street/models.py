from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Street(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=140)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='upload_location',
            null=True, blank=True,
            width_field='width_field',
            height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id':self.id})
