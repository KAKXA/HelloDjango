from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# urls.py刚刚添加了对应着index的路径:''(即根目录)
def index(req):
    return HttpResponse('hello, this is Ge\'s blog')