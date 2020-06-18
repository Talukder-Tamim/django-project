from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    full_name = models.CharField(max_length=30)
    photo = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class About(models.Model):
    body = models.TextField()

class Contact(models.Model):
    contact = models.TextField()
