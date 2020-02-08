from django.db import models
from ckeditor.fields import RichTextField
from django import forms


# Create your models here.
# 科目类型类
class Course(models.Model):
    course_name = models.CharField(max_length=32, verbose_name='科目名称')
    course_img = models.ImageField(upload_to='images', verbose_name='科目图片')

    def __str__(self):
        return self.course_name  # 返回用户名

    class Meta:
        db_table = 'course'
        verbose_name = '科目'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示


# 文章类
class Article(models.Model):
    art_title = models.CharField(max_length=32, verbose_name='文章标题')
    art_description = RichTextField(verbose_name='文章描述')
    art_content = RichTextField(verbose_name='文章内容')
    art_img = models.ImageField(upload_to='images', verbose_name='文章图片')
    art_date = models.DateField(auto_now_add=True, verbose_name='发布时间')
    art_click = models.IntegerField(default=0, verbose_name='点击率')
    art_recommend = models.IntegerField(default=0, verbose_name='推荐状态')
    art_type = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='类型外键')

    # art_click = models.ForeignKey(to=Click, on_delete=models.CASCADE, verbose_name='点击外键')

    def __str__(self):
        return self.art_title  # 返回用户名

    class Meta:
        db_table = 'article'
        verbose_name = '文章'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示


# 旅游城市类
class City(models.Model):
    city_name = models.CharField(max_length=32, verbose_name='旅游地点')
    city_img = models.ImageField(upload_to='images', verbose_name='标志图片')
    city_description = RichTextField(verbose_name='城市描述')

    def __str__(self):
        return self.city_name  # 返回用户名

    class Meta:
        db_table = 'city'
        verbose_name = '城市'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示


# 城市景点类
class Images(models.Model):
    spot_img = models.ImageField(upload_to='images', verbose_name='景点图片')
    images_type = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name='城市外键')

    class Meta:
        db_table = 'images'
        verbose_name = '照片'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示


# 留言类
class Comment(models.Model):
    comment = models.TextField(verbose_name='留言内容')
    date = models.DateField(auto_now=True, verbose_name='发布时间')

    class Meta:
        db_table = 'comment'
        verbose_name = '留言'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示
