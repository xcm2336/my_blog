# Generated by Django 2.0.5 on 2018-05-27 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_visit_Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_read_time', models.DateTimeField(auto_now_add=True, verbose_name='第一次浏览时间')),
                ('last_read_time', models.DateTimeField(auto_now=True, verbose_name='最近一次浏览时间')),
                ('counter', models.PositiveIntegerField(default=1, verbose_name='访问次数')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
                ('web', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user_visit_blog',
            unique_together={('user', 'web')},
        ),
    ]
