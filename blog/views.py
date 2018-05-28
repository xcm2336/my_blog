from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import *
import markdown
from django.http import Http404

#返回一些基本数据，包括所有的专栏和对应的文章数，最热的5篇文章，所有的标签
def get_base_information(request):

    categories = Category.objects.all()
    catelist = []
    for c in categories:
        t = Blog_Category_Relation.objects.filter(category=c)
        catelist.append((c, len(t)))
    catelist.sort(key=lambda cl: cl[1], reverse=True)

    blogs = Blog.objects.all()
    latest = blogs.order_by('-id')
    top5 = blogs.order_by('-visitedtime')
    top5 = top5[:5]

    tags = Tag.objects.all()
    return {'catelist': catelist, 'top5': top5, 'tags': tags}


def main_page(request):
    blogs = Blog.objects.all();
    latest3 = blogs.order_by('-id')[:3]
    hottest3 = blogs.order_by('-visitedtime')[:3]

    return render(request,'home.html',{'latest3': latest3, 'hottest3': hottest3})


def blog_main_page(request):
    blogs = Blog.objects.all()
    latest =blogs.order_by('-id')
    top5 = blogs.order_by('-visitedtime')

    categories = Category.objects.all()
    catelist = []
    for c in categories:
        t = Blog_Category_Relation.objects.filter(category=c)
        catelist.append((c,len(t)))
    catelist.sort(key=lambda cl: cl[1], reverse=True)
    tags = Tag.objects.all()
    #分页
    bcounts = len(blogs)
    if bcounts > 5:
        blogs = latest[:5]
    top5 = top5[:5]
    pagenumber = range(1, (bcounts // 5) + 2)

    return render(request, 'blog_main_page.html', {'latest': blogs, 'pagenumber': pagenumber, 'blogcount': bcounts,
                                                   'catelist': catelist, 'top5': top5, 'tags': tags})


def blog_single_page(request,bid):
    blog = get_object_or_404(Blog, pk=bid)
    blog.increase_views()


    #ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", None))

    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
    except KeyError:
        pass
    else:
        real_ip = real_ip.split(",")[0]

        request.META['REMOTE_ADDR'] = real_ip

    ip = request.META.get("REMOTE_ADDR",None)



    try:
        user = get_object_or_404(User, ip=ip)
        user_blog = get_object_or_404(User_visit_Blog,user=user,web=blog)
        user_blog.counter += 1
        user_blog.save(update_fields=['last_read_time','counter'])
    except Http404:
        if user == None:
            user = User(ip=ip)
            user_blog = User_visit_Blog(user=user,web=blog)
            user.save()
            user_blog.save()
        else:
            user_blog = User_visit_Blog(user=user,web=blog)
            user_blog.save()


    blog.blog_text = markdown.markdown(blog.blog_text,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
    categoriesrelation = Blog_Category_Relation.objects.filter(blog=blog)
    countlist = []
    categories = []
    tags=[]

    for c in categoriesrelation:
        categories.append(c.category)

    for c in categories:
        t = Blog_Category_Relation.objects.filter(category=c)
        countlist.append((c, len(t)))

    tagsrelation = Blog_Tag_Relation.objects.filter(blog=blog)
    for t in tagsrelation:
        tags.append(t.tag)

    return render(request,'blog_single_page.html', {'blog': blog, 'list': countlist, 'tags': tags})


def blog_pages(request, pagenumber):
    allblog = Blog.objects.all().order_by('-id')
    top5 = allblog.order_by('-visitedtime')
    top5 = top5[:5]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    catelist = []
    for c in categories:
        t = Blog_Category_Relation.objects.filter(category=c)
        catelist.append((c, len(t)))
    catelist.sort(key=lambda cl: cl[1], reverse=True)
    counts = len(allblog)
    if counts > 5:
        startpos = (pagenumber - 1) * 5
        endpos = min(counts, (pagenumber * 5))
        blogs = allblog[startpos:endpos]
    pagecount = range(1, (counts // 5) + 2)
    return render(request, 'blog_pages.html', {'latest': blogs, 'pagecount': pagecount, 'pagenumber': pagenumber,
                                                   'catelist': catelist, 'top5': top5, 'tags': tags})


def category_main_page(request):
    blogs = Blog.objects.all()
    top5 = blogs.order_by('-visitedtime')
    categories = Category.objects.all()
    catelist = []
    for c in categories:
        t = Blog_Category_Relation.objects.filter(category=c)
        catelist.append((c, len(t)))
    catelist.sort(key=lambda cl: cl[1], reverse=True)
    tags = Tag.objects.all()
    top5 = top5[:5]

    return render(request, 'category_main_page.html', {'catelist': catelist, 'top5': top5, 'tags': tags})


def category_single_page(request,cid):
    dict = get_base_information(request)
    category = Category.objects.get(id=cid)
    blogs = Blog_Category_Relation.objects.filter(category=category)
    bloglist = []
    for blog in blogs:
        bloglist.append(blog.blog)

    dict['bloglist']=bloglist

    pagenumber = (len(bloglist) // 6) + 1

    pagenumber = range(1,pagenumber+1)

    dict['pagenumber']=pagenumber
    dict['category']=category

    return render(request, 'category_single_page.html', dict)


def tag_page(request,tid):
    dict = get_base_information(request)
    tag = Tag.objects.get(id=tid)
    blogs = Blog_Tag_Relation.objects.filter(tag=tid)
    bloglist = []
    for blog in blogs:
        bloglist.append(blog.blog)

    dict['bloglist'] = bloglist

    pagenumber = (len(bloglist) // 6) + 1

    pagenumber = range(1, pagenumber + 1)

    dict['pagenumber'] = pagenumber
    dict['tag'] = tag

    return render(request, 'tag_page.html', dict)

