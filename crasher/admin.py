from django.contrib import admin

# Register your models here.
from . models import Crasher

class CrasherModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']

    class Meta:
        model = Crasher

admin.site.register(Crasher, CrasherModelAdmin)
