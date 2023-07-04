from django.contrib.auth.models import User
from django.db import models


class Viewer(models.Model):
    ipaddress = models.GenericIPAddressField("Ip", blank=True, null=True)
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Picture(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=130, unique=True, blank=True)
    views = models.ManyToManyField(Viewer, blank=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='picture_likes', blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='', blank=True, default='no-image-available.jpg')

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='picture_review')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content

