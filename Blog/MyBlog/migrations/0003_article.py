# Generated by Django 2.2.1 on 2019-11-27 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0002_auto_20191127_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('art_description', models.TextField(verbose_name='文章描述')),
                ('art_content', models.TextField(verbose_name='文章内容')),
                ('art_img', models.ImageField(upload_to='images', verbose_name='文章图片')),
                ('art_date', models.DateField(auto_now=True, verbose_name='发布时间')),
                ('art_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.Course', verbose_name='类型外键')),
            ],
            options={
                'db_table': 'article',
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]