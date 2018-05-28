from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Blog(models.Model):#还是要一个用户，要不然被访问了记录不了ip地址
    id = models.AutoField(primary_key=True)
    visitedtime = models.PositiveIntegerField("访问次数", default=0, editable=False)
    title = models.CharField("标题", max_length=50)
    publish_date = models.DateTimeField("发布时间",auto_now_add=True)
    modified_date = models.DateTimeField("最后修改时间", auto_now=True)
    blog_text = RichTextField("博客正文", default="请输入你的博客")

    def increase_views(self):
        self.visitedtime += 1
        self.save(update_fields=['visitedtime'])

    def __str__(self):
        return self.title
    pass


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("标签名称", max_length=30, unique=True)

    def __str__(self):
        return self.name
    pass


class Blog_Tag_Relation(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('blog', 'tag')

    def __str__(self):
        return self.blog.title + '--' + self.tag.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("专栏名称", max_length=30, unique=True)

    def __str__(self):
        return self.name
    pass


class Blog_Category_Relation(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('blog', 'category')

    def __str__(self):
        return self.blog.title + '--' + self.category.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=16)

    def __str__(self):
        return self.ip


class User_visit_Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    web = models.ForeignKey(Blog,on_delete=models.CASCADE)
    first_read_time = models.DateTimeField("第一次浏览时间",auto_now_add=True)
    last_read_time = models.DateTimeField("最近一次浏览时间",auto_now=True)
    counter = models.PositiveIntegerField("访问次数",default=1)
    class Meta:
        unique_together = ('user', 'web')

class Comment(models.Model):
    pass


