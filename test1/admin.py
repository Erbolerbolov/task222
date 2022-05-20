from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields if field.name]


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields if field.name]



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

