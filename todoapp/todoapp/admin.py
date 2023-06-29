from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('tasks', 'is_completed', 'updated_at')
    search_fields = ('tasks',)
admin.site.register(Todo, TodoAdmin)