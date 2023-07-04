from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display_links = ('username',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'created')

