from django.urls import path

from . import views

# 命名空间
app_name = 'blog'
urlpatterns = [
    # 在根目录'',对应的视图在views中的index函数,名字是index
    path('', views.index, name='index'),
    # 如果<int:pk>到1,就把1作为views.detail的关键字
    # 实际上的视图函数调用是 detail(request, pk=1)
    path('post/<int:pk>/', views.detail, name='detail'),
]