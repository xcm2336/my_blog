from django.shortcuts import render
from django.views.decorators import csrf
from .models import *
from .views import *

# 接收POST请求数据
def search_post(request):

    dict = get_base_information(request)
    kws = request.GET['kw']

    blogs = Blog.objects.filter(blog_text__contains=kws)
    dict['bloglist'] = blogs
    dict['kw'] = kws

    return render(request, "search_page.html",dict)