from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    # 定义一个继承ModelAdmin的类
    # 这样可以自定义admin Post提供更详细的信息
    list_display = ["title", "created_time", "modified_time", "category", "author"]

    # field属性用来控制表单展现的字段
    # 由于创建时间不用让用户来填,所以不在待填写的表单中展现
    fields = ["title", "body", "excerpt", "category", "tags"]

    def save_model(self, request, obj, form, change) -> None:
        # 用户自动填入当前request的发起用户
        obj.author = request.user
        return super().save_model(request, obj, form, change)


# Register your models here.
# 把新增的 Postadmin也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
