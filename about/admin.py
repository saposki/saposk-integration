from django.contrib import admin

# Register your models here.
from . models import About

class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    # list_display_links = ?
    class Meta:
        model = About

admin.site.register(About, AboutModelAdmin)
