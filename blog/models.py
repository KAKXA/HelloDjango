from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# 一个分类名
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章的数据库表
# 这个类表示了一篇文章的各种元素
class Post(models.Model):
    # 一篇博文的标题,限制长度为70
    title = models.CharField('标题', max_length=70)
    # 因为一篇文章的正文是一大串文字,所以应该用TextField
    body = models.TextField('正文')
    # 分别表示文章的创建时间和最后一次修改时间 
    # 在用户没有指定时,时间默认为当前时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')

    # 摘要(令blank=True使得允许空的摘要)
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 规定一篇文章只能一种分类,所以用ForeignKey,它是一种一对多模型 
    # 在一种分类被删除时,默认属于这个分类的文章也删除,所以on_delete=models.CASCADE
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    # 规定文章和tag是多对多的关系,所以用ManyToManyField
    # 允许文章没有Tag,所以blank=True
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签(Tag)')

    # 规定一个作者可以有多篇文章,所以用ForeignKey 
    # 作者消失,他写的文章也消失
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者(测试)')

    # 配置model特性是通过model的内部类来定义的
    class Meta:
        # 定义冗长名
        verbose_name = '文章'
        # 定义复数形式
        verbose_name_plural = verbose_name
    
    
    # 重写save方法,保证在每次save时都改变modified_time的值
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title