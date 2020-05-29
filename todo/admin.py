from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'date', 'is_complete')


admin.site.register(Todo, TodoAdmin)

