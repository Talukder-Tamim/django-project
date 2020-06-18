from django.contrib import admin
from .models import Post, Category, Profile, Contact, About

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(About)