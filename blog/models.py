from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 一个分类名
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章的数据库表
# 这个类表示了一篇文章的各种元素
class Post(models.Model):
    # 一篇博文的标题,限制长度为70
    title = models.CharField(max_length=70)
    # 因为一篇文章的正文是一大串文字,所以应该用TextField
    body = models.TextField()
    # 分别表示文章的创建时间和最后一次修改时间 
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要(令blank=True使得允许空的摘要)
    excerpt = models.CharField(max_length=200, blank=True)

    # 规定一篇文章只能一种分类,所以用ForeignKey,它是一种一对多模型 
    # 在一种分类被删除时,默认属于这个分类的文章也删除,所以on_delete=models.CASCADE
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 规定文章和tag是多对多的关系,所以用ManyToManyField
    # 允许文章没有Tag,所以blank=True
    tags = models.ManyToManyField(Tag, blank=True)

    # 规定一个作者可以有多篇文章,所以用ForeignKey 
    # 作者消失,他写的文章也消失
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title