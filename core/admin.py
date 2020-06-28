from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *




@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Mix)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', ]
    list_filter = ['user__the_group']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    pass
