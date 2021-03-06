import xadmin
from .models import CourseInfo


class CourseInfoXadmin(object):
    list_display = ['id', 'name', 'term', 'course_time', 'course_grade', 'department', 'teacher', 'address', 'add_time']
    model_icon = 'fa fa-book'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


xadmin.site.register(CourseInfo, CourseInfoXadmin)