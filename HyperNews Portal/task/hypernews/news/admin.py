from django.contrib import admin

from .models import NewsPost, PostComment

# Register your models here.
admin.site.register(NewsPost)
admin.site.register(PostComment)
