# Generated by Django 2.2.1 on 2019-12-01 16:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=32, verbose_name='科目名称')),
                ('course_img', models.ImageField(upload_to='images', verbose_name='科目图片')),
            ],
            options={
                'verbose_name_plural': '科目',
                'db_table': 'course',
                'verbose_name': '科目',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('art_description', ckeditor.fields.RichTextField(verbose_name='文章描述')),
                ('art_content', ckeditor.fields.RichTextField(verbose_name='文章内容')),
                ('art_img', models.ImageField(upload_to='images', verbose_name='文章图片')),
                ('art_date', models.DateField(auto_now_add=True, verbose_name='发布时间')),
                ('click', models.IntegerField(default=0, verbose_name='点击率')),
                ('recommend', models.IntegerField(default=0, verbose_name='推荐状态')),
                ('art_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.Course', verbose_name='类型外键')),
            ],
            options={
                'verbose_name_plural': '文章',
                'db_table': 'article',
                'verbose_name': '文章',
            },
        ),
    ]
