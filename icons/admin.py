from django.contrib import admin

from .models import Viewer, Icons, Category


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'user')


@admin.register(Icons)
class IconsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'category', 'author',  'description')
    list_display_links = ('name', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'created')
