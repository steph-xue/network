from django.contrib import admin
from .models import User, Post, Follow, Like, Dislike

# Registers the app's models so they appear in the Django admin site
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Dislike)