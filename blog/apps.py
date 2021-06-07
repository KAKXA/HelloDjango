from django.apps import AppConfig
from django.db import models


class BlogConfig(AppConfig):
    name = "blog"
    # 要修改app在后台的显示名字,添加verbose_name
    verbose_name = "博客"
