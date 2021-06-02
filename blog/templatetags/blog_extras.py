from django import template

from ..models import Post, Category, Tag

register = template.Library()


# 最新文章模板标签
# 将show_recent_posts装饰为register.inclusion_tag
# 所以这个函数是我们自定义的一个类型为inclusion_tag的模板标签
# inclusion_tag模板标签和视图函数的功能类似，返回一个字典，值为模板变量
# 参数takes_context设置为True时,渲染_recent_posts.html模板时不仅传入模板变量,
# 还会返回覆膜板的上下文()
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }

# 归档模板标签
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }

# 分类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

# 标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }

