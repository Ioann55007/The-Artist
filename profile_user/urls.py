from django.urls import path

from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', views.ProfileUpdate.as_view(), name='edit'),
    path('api/edit/<int:pk>/', views.ProfileApi.as_view())
]
