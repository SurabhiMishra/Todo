from django.contrib import admin
from .models import todo

class todoadmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(todo,todoadmin)
