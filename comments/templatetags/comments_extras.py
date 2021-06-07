from comments.views import comment
from django import template
from ..forms import CommentForm

register = template.Library()

# 这个装饰器的功能是把被装饰的函数的返回值(一个字典)发给第一个参数
# 即模板的路径
@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form, 
        'post': post,
    }

@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        # 也可以直接在模板中调用
        'comment_count': comment_count,
        'comment_list': comment_list
    }