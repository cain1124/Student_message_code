from django.db import models
from datetime import datetime
from department.models import DepartmentInfo


# Create your models here.
class CourseInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='课程名称')
    term = models.CharField(max_length=100, verbose_name='上课学期')
    course_time = models.IntegerField(verbose_name='课程学时')
    course_grade = models.IntegerField(verbose_name='课程学分')
    department = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE, verbose_name='所属学院')
    category = models.IntegerField(choices=((1, '公共基础课'), (2, '公共选修课'), (3, '专业基础课'), (4, '专业方向课'), (5, '专业选修课')),
                                   verbose_name='课程类别', null=True, blank=True)
    teacher = models.CharField(max_length=20, verbose_name='授课教师')
    address = models.CharField(max_length=200, verbose_name='上课时间地点')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

