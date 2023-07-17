from django.urls import path

from . import views
app_name = 'icon'

urlpatterns = [
    path('icons/', views.ViewIcon.as_view(), name='icons'),
    path('icons/<slug:slug>/', views.DetailIcon.as_view(), name='icon'),
    path('delete_review_icon/<int:id>/', views.delete_review, name='delete-review'),
    path('icon_like/<int:id>', views.like, name='add_like')


]