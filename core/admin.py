from django.contrib import admin
from .models import *




@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Mix)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', ]
    list_filter = ['user__group']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
