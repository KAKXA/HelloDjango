from django.http import HttpResponse
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
import re


# 所有post的列表
def index(req):
    post_list = Post.objects.all().order_by("-created_time")
    return render(req, "blog/index.html", context={"post_list": post_list})


# urls.py刚刚添加了对应着index的路径:''(即根目录)
# def index(req):
#     # context传入index.html作为其中{{}}包含的元素的替代
#     return render(req, 'blog/index.html', context={
#         'title': 'Ge\'s blog main page',
#         'welcome': 'Welcome to my main page'
#     })
#     return HttpResponse('hello, this is Ge\'s blog')


def detail(request, pk):
    # 如果object存在就返回object否则返回404
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            # 'markdown.extensions.toc',
            # 处理标题的锚点值
            TocExtension(slugify=slugify),
        ]
    )
    # 用convert方法将post.body中地Markdown文本解析成HTML文本
    post.body = md.convert(post.body)
    # 在经过上面这行以后,md拥有了toc属性

    # 正则表达式检查目录是否为空
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)

    # 如果未匹配到目录内容就把post.toc置为空
    # 为post实例动态地添加了toc属性
    post.toc = m.group(1) if m is not None else ""

    # render 是将给定的模板和上下文和上下文字典组合
    # 此时post.body是经过markdown解析过后的HTML文本
    return render(request, "blog/detail.html", context={"post": post})


def archive(request, year, month):
    # 筛出指定年和月的文章
    post_list = Post.objects.filter(
        created_time__year=year, created_time__month=month
    ).order_by("-created_time")
    # 界面和index.html一样,只不过只展示在指定年月发布的文章
    return render(request, "blog/index.html", context={"post_list": post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by("-created_time")
    return render(request, "blog/index.html", context={"post_list": post_list})
