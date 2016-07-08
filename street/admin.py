from django.contrib import admin

# Register your models here.
from . models import Street

class StreetModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']

    class Meta:
        model = Street

admin.site.register(Street, StreetModelAdmin)
