from django.db import models
from datetime import datetime


# Create your models here.
class DepartmentInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='学院名称')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='学院简介')
    student_num = models.IntegerField(default=0, verbose_name='院学生人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学院信息'
        verbose_name_plural = verbose_name


class MajorInfo(models.Model):
    department = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE, verbose_name='所属学院')
    name = models.CharField(max_length=200, verbose_name='专业名称')
    student_num = models.IntegerField(default=0, verbose_name='专业学生人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业信息'
        verbose_name_plural = verbose_name


class ClassInfo(models.Model):
    major = models.ForeignKey(MajorInfo, on_delete=models.CASCADE, verbose_name='所属专业')
    name = models.CharField(max_length=200, verbose_name='班级名称')
    student_num = models.IntegerField(default=0, verbose_name='班级人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name


