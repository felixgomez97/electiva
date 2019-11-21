from django.contrib import admin
from .models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Notice, NoticeAdmin)