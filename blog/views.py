from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404


# 所有post的列表
def index(req):
    post_list = Post.objects.all().order_by('-created_time')
    return render(req, 'blog/index.html', context={'post_list': post_list})
# urls.py刚刚添加了对应着index的路径:''(即根目录)
# def index(req):
#     # context传入index.html作为其中{{}}包含的元素的替代
#     return render(req, 'blog/index.html', context={
#         'title': 'Ge\'s blog main page',
#         'welcome': 'Welcome to my main page'
#     })
#     return HttpResponse('hello, this is Ge\'s blog')
def detail(req, pk):
    # 如果object存在就返回object否则返回404
    post = get_object_or_404(Post, pk=pk)
    # render 是将给定的模板和上下文和上下文字典组合
    return render(req, 'blog/detail.html', context={'post': post})