# Generated by Django 2.0.5 on 2018-05-27 03:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('visitedtime', models.PositiveIntegerField(default=0, editable=False, verbose_name='访问次数')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('blog_text', ckeditor.fields.RichTextField(default='请输入你的博客', verbose_name='博客正文')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Category_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Tag_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='专栏名称')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='blog_tag_relation',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='blog_category_relation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='blog_tag_relation',
            unique_together={('blog', 'tag')},
        ),
        migrations.AlterUniqueTogether(
            name='blog_category_relation',
            unique_together={('blog', 'category')},
        ),
    ]
