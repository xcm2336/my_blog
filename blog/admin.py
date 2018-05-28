from django.contrib import admin

# Register your models here.
from .models import *


class Blog_Tag(admin.StackedInline):
    model = Blog_Tag_Relation
    extra = 0


class Blog_Category(admin.StackedInline):
    model = Blog_Category_Relation
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'blog_text')
    list_display_links = ('id', 'title')
    list_display = ('id', 'title', 'publish_date', 'modified_date', 'visitedtime')
    list_filter = ['publish_date', 'modified_date']
    date_hierarchy = 'publish_date'
    inlines = [Blog_Tag, Blog_Category]

    fieldsets = [
        (None, {'fields': ['title']}),
        ("博客", {'fields': ['blog_text']}),
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [Blog_Tag]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [Blog_Category]


class Blog_Tag_Admin(admin.ModelAdmin):
    list_filter = ['tag__name', 'blog__title']


class Blog_Category_Admin(admin.ModelAdmin):
    list_filter = ['category__name', 'blog__title']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','ip']
    readonly_fields = ('ip',)


class User_Blog_Admin(admin.ModelAdmin):
    list_display = ['user', 'web', 'first_read_time', 'last_read_time', 'counter']
    list_filter = ['user__ip','web__title']
    readonly_fields = ('user','web','counter')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog_Category_Relation,Blog_Category_Admin)
admin.site.register(Blog_Tag_Relation, Blog_Tag_Admin)
admin.site.register(User,UserAdmin)
admin.site.register(User_visit_Blog,User_Blog_Admin)