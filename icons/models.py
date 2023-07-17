from django.contrib.auth.models import User
from django.db import models


class Viewer(models.Model):
    objects = models.Manager()
    ipaddress = models.GenericIPAddressField("IP address", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_viewer')


class Icon(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=130, unique=True, blank=True)
    viewers = models.ManyToManyField(Viewer, blank=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='icon_author')
    icon_likes = models.ManyToManyField(User,  blank=True, related_name='icon_likes')
    description = models.TextField()
    image = models.ImageField(upload_to='', blank=True, default='no-image-available.jpg')

    def __str__(self):
        return self.name

    def count_likes(self):
        return self.icon_likes.count()




class Category(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_author')
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, related_name='icon_review')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content

