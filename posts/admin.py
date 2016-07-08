from django.contrib import admin

# Register your models here.
from .models import Post #using relative import with '.' instead of 'posts.model'

admin.site.register(Post)
