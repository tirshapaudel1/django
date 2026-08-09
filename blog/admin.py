from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
admin.site.site_header = "Blog CMS Administration"
admin.site.site_title = "Blog CMS Admin Portal"
admin.site.index_title = "Welcome to Blog CMS Portal"
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)