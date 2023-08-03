from django.urls import path

from . import views
app_name = 'pictures'

urlpatterns = [
    path('pictures/', views.ViewPicture.as_view(), name='pictures'),
    path('pictures/<slug:slug>/', views.DetailPicture.as_view(), name='picture'),
    path('delete_review/<int:id>/', views.delete_review, name='delete-review'),
    path('like/<int:id>', views.like, name='add_like'),
    path('api/picture/', views.PictureApiView.as_view()),
    # path('picture/new/', views.NewPictureView.as_view())

]
