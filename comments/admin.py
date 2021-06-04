from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    # 显示但不可修改
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    # 可以允许用户修改
    fields = ['name', 'email', 'url', 'text', 'post']

admin.site.register(Comment, CommentAdmin)