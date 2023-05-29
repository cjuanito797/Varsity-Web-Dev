from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', ]
