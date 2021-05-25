from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# urls.py刚刚添加了对应着index的路径:''(即根目录)
def index(req):
    # context传入index.html作为其中{{}}包含的元素的替代
    return render(req, 'blog/index.html', context={
        'title': 'Ge\'s blog main page',
        'welcome': 'Welcome to my main page'
    })
    return HttpResponse('hello, this is Ge\'s blog')