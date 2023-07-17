from django.urls import path

from .import views

urlpatterns = [
    path('', views.first_page, name='first'),
    path('about_me/', views.AboutView.as_view(), name='about'),
    path('deliver/', views.DeliverView.as_view(), name='deliver'),
    path('confined/', views.Confiden.as_view(), name='confined'),
    path('rule/', views.TheRule.as_view(), name='rules'),
]
