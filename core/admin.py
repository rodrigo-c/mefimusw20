from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Mix)
class SubmissionAdmin(admin.ModelAdmin):
    pass
    # list_display = ['user', 'user__mefi_handle']
    list_filter = ['user__the_group']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['mefi_handle', 'the_group', 'platform']
    list_filter = ['the_group', 'platform']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'groups',)}),
        ('Swap', {'fields': ('mefi_handle', 'the_group', 'platform',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    list_editable = ['the_group']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_object', 'short' ]