from django.contrib import admin

# Register your models here.
from . models import Portrait

class PortraitModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp', 'updated']

    class Meta:
        model = Portrait

admin.site.register(Portrait, PortraitModelAdmin)
