from django.db import models
from ckeditor.fields import RichTextField


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
    art_date = models.DateField(auto_now=True, verbose_name='发布时间')
    art_type = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='类型外键')

    def __str__(self):
        return self.art_title  # 返回用户名

    class Meta:
        db_table = 'article'
        verbose_name = '文章'  # 站点中以中文显示表名
        verbose_name_plural = verbose_name  # 默认以复数显示
