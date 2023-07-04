from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Viewer(models.Model):
    ipaddress = models.GenericIPAddressField("Ip", blank=True, null=True)
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='icon_user')


class Icons(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=130, unique=True, blank=True)
    views = models.ManyToManyField(Viewer, blank=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='icon_likes', blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='', blank=True, default='no-image-available.jpg')


class Category(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
