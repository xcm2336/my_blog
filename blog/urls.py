from django.urls import path,include
from django.conf.urls import url
from blog import views

urlpatterns = [
    path('', views.blog_main_page),
    path('<int:bid>/',views.blog_single_page),
    path('page/<int:pagenumber>',views.blog_pages),
    path('category/<int:cid>',views.category_single_page),
    path('category/',views.category_main_page),
    path('tag/<int:tid>',views.tag_page),
]