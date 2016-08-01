from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
