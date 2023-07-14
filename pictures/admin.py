from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from . models import Viewer, Picture, Category, Review


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'user')


@admin.register(Picture)
class IconsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'category', 'author',  'description')
    list_display_links = ('name', 'author')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'created')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display_links = ('author',)
    list_display = ('author', 'created', 'content', 'picture')






