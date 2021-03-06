import xadmin
from .models import ScourseInfo, RewardInfo, StudentMessage


class ScourseInfoXadmin(object):
    list_display = ['id', 'student', 'course', 'type', 'reason', 'course_cj', 'add_time']
    model_icon = 'fa fa-info'
    search_fields = ['student', 'course', 'type']
    # 要搜索的字段

    list_filter = ['course', 'type']
    # 要筛选的字段

    list_editable = ['type', 'reason', 'course_cj']
    # 列表可直接修改的字段

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


class RewardInfoXadmin(object):
    list_display = ['student', 'message', 'add_time']
    model_icon = 'fa fa-info-circle'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


class StudentMessageXadmin(object):
    list_display = ['message_student', 'message_content', 'message_status', 'add_time']
    list_editable = ['message_status', 'message_content']
    # 列表可直接修改的字段
    model_icon = 'fa fa-commenting-o'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


xadmin.site.register(ScourseInfo, ScourseInfoXadmin)
xadmin.site.register(RewardInfo, RewardInfoXadmin)
xadmin.site.register(StudentMessage, StudentMessageXadmin)
