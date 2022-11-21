# Register your models here.
from django.contrib import admin

from apps.monolit.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
