from django.urls import path

from . import views

urlpatterns = [
    # 在根目录'',对应的视图在views中的index函数,名字是index
    path('', views.index, name='index'),
]