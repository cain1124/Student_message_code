from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from department.models import MajorInfo, DepartmentInfo, ClassInfo


# Create your models here.
class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='student/', max_length=200, verbose_name='学生照片', null=True, blank=True)
    xm = models.CharField(max_length=20, verbose_name='姓名', null=True, blank=True)
    xh = models.CharField(max_length=10, verbose_name='学号', null=True, blank=True)
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), max_length=10, verbose_name='性别', default='boy')
    cardid = models.CharField(max_length=18, verbose_name='身份证号', null=True, blank=True)
    nation = models.CharField(max_length=10, verbose_name='民族', null=True, blank=True)
    politics_status = models.CharField(choices=(('qz', '群众'), ('gqt', '共青团员'), ('gcd', '共产党员')), max_length=10,
                                       default='qz', verbose_name='政治面貌', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='手机', null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name='家庭住址', null=True, blank=True)
    grade = models.CharField(max_length=8, verbose_name='年级', null=True, blank=True)
    xuezhi = models.IntegerField(choices=((2, '2年'), (3, '3年'), (4, '4年'), (5, '5年')), default=4, verbose_name='学制')
    time = models.DateField(verbose_name='入学时间', null=True, blank=True)
    student_class = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, verbose_name='所属班级', null=True, blank=True)
    student_major = models.ForeignKey(MajorInfo, on_delete=models.CASCADE, verbose_name='所属专业', null=True, blank=True)
    student_department = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE, verbose_name='所属学院', null=True, blank=True)
    category = models.IntegerField(choices=((1, '全日制专业学位硕士'), (2, '全日制学业学位硕士'), (3, '全日制本科学位')), verbose_name='学生类别',null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.username

    #
    def get_msg_counter(self):
        from behavior.models import StudentMessage
        counter = StudentMessage.objects.filter(message_student=self.id, message_status=False).count()
        return counter

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class StudentUser(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='导入学生')

    def __str__(self):
        return self.user.xm

    class Meta:
        verbose_name = '导入学生信息'
        verbose_name_plural = verbose_name


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=200, verbose_name='验证码邮箱')
    send_type = models.IntegerField(choices=((1, 'register'), (2, 'forget'), (3, 'change')), verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码信息'
        verbose_name_plural = verbose_name

