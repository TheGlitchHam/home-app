"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from todo.views import api_root, TodoViewSet, CategoryViewSet


todo_list = TodoViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

todo_detail = TodoViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

category_list = CategoryViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

category_detail = CategoryViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)


urlpatterns = [
    path('', api_root),
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:pk>', todo_detail, name='todo_detail'),
    #path('todos/<int:pk>/highlight/', views.TodoHighlights.as_view(), name='todo_highlight'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>',
         category_detail, name='category_details'),

]
