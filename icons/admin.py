from django.contrib import admin

from .models import Viewer, Icon, Category, Review


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'user')


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
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
    list_display = ('author', 'created', 'content', 'icon')