from django import forms
from django.forms import fields
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 说明对应的数据库模型是 models.Comment
        model = Comment
        # 只显示以下四个, 填完以后传到数据库去存起来
        fields = ["name", "email", "url", "text"]
