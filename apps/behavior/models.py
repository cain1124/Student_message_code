from django.db import models
from datetime import datetime
from users.models import UserProfile
from course.models import CourseInfo


# Create your models here.
class ScourseInfo(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='选课学生')
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='申请课程')
    course_cj = models.IntegerField(verbose_name='课程成绩', null=True, blank=True)
    type = models.CharField(choices=(('申请', '申请'), ('退选', '退选'), ('已选', '已选')), null=True, blank=True, max_length=20, verbose_name='申请类型')
    reason = models.CharField(max_length=200, null=True, blank=True, verbose_name='申请原因')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='选课时间')

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = '选课信息'
        verbose_name_plural = verbose_name


class RewardInfo(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='获奖学生')
    message = models.CharField(max_length=300, verbose_name='奖惩情况')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.student.xm

    class Meta:
        verbose_name = '奖惩信息'
        verbose_name_plural = verbose_name


class StudentMessage(models.Model):
    message_student = models.IntegerField(default=0, verbose_name='消息学生')
    message_content = models.CharField(max_length=300, verbose_name='消息内容')
    message_status = models.BooleanField(default=False, verbose_name='消息状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.message_content

    class Meta:
        verbose_name = '学生消息信息'
        verbose_name_plural = verbose_name
