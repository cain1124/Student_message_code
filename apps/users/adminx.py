import xadmin
from .models import EmailVerifyCode, UserProfile, StudentUser
from xadmin import views
from import_export import resources
from department.models import *
from behavior.models import *
from course.models import *


#配置xadmin的主题，注册时要用到专用的view取注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class StudentUserResource(resources.ModelResource):

    class Meta:
        model = UserProfile
        # 导出类型
        list_export = True
        # #list_export设置为None来禁用数据导出功能
        # 导出字段
        # list_export_fields = ('start_people', 'sport', 'sport_time')
        skip_unchanged = True       # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True       # 在导入预览页面中显示跳过的记录
        # import_id_fields = ('id',)  # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = ('id',
                  'username',
                  'xm',
                  'xh',
                  'gender',
                  'cardid',
                  'nation',
                  'phone',
                  'address',
                  'category',
                  'email',
                  'password',
                  'student_department',
                  'student_major',
                  'time')# 白名单
        # exclude = () 黑名单


class StudentUserXadmin(object):
    list_display = ['user']
    # 要显示的字段列表

    ordering = ['id']
    # 按照id顺序排列，如果是倒序-id

    search_fields = ['user']
    # 要搜索的字段

    list_filter = ['user']
    # 要筛选的字段

    show_detail_fields = ['user']
    # 要展示详情的字段

    list_editable = ['user']
    # 列表可直接修改的字段

    list_per_page = 10
    # 分页

    model_icon = 'fa fa-building'
    # 配置模型图标，也可以在GlobalSetting里面配置

    import_export_args = {
        'import_resource_class': StudentUserResource,
        # 'export_resource_class': DepartmentInfoResource,
    }
    # 配置导入按钮


class CommXadminSetting(object):
    site_title = '学生信息后台管理系统'
    site_footer = '学生信息管理系统'
    menu_style = 'accordion'#菜单列表样式
    # apps_icons = {
    #     "product": "fa fa-music",
    # } # 配置应用图标，即一级菜单图标

    # 自定义菜单显示
    def get_site_menu(self):
        return (
            {'title': '院系模块', 'icon': 'fa fa-fort-awesome', 'menus': (
                {'title': '学院信息', 'icon': 'fa fa-building', 'url': self.get_model_url(DepartmentInfo, 'changelist')},
                {'title': '专业信息', 'icon': 'fa fa-building-o', 'url': self.get_model_url(MajorInfo, 'changelist')},
                {'title': '班级信息', 'icon': 'fa fa-university', 'url': self.get_model_url(ClassInfo, 'changelist')},
            )},
            {'title': '用户模块', 'icon': 'fa fa-user-circle', 'menus': (
                {'title': '学生信息', 'icon': 'fa fa-user', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '邮箱验证码信息', 'icon': 'fa fa-envelope', 'url': self.get_model_url(EmailVerifyCode, 'changelist')},
                {'title': '导入学生信息', 'icon': 'fa fa-user-o', 'url': self.get_model_url(StudentUser, 'changelist')},
            )},
            {'title': '课程模块', 'icon': 'fa fa-leanpub', 'menus': (
                {'title': '课程信息', 'icon': 'fa fa-book', 'url': self.get_model_url(CourseInfo, 'changelist')},
            )},
            {'title': '操作模块', 'icon': 'fa fa-pencil-square-o', 'menus': (
                {'title': '选课信息', 'icon': 'fa fa-info', 'url': self.get_model_url(ScourseInfo, 'changelist')},
                {'title': '奖惩信息', 'icon': 'fa fa-info-circle', 'url': self.get_model_url(RewardInfo, 'changelist')},
                {'title': '学生消息', 'icon': 'fa fa-commenting-o', 'url': self.get_model_url(StudentMessage, 'changelist')},
            )},
        )


class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']
    search_fields = ['code', 'email', 'send_type']  # 搜索
    list_filter = ['code', 'email', 'send_type']  # 过滤器
    list_editable = ['send_type']  # 列出可编辑的字段
    # 每页显示多少条
    list_per_page = 20
    # 根据id排序
    ordering = ['id']
    # 设置只读字段　
    readonly_fields = ('email',)
    # 显示本条数据的所有信息
    show_detail_fields = ['asset_name']
    # list_export = ('xls', 'xml', 'json')  #设置数据导出格式
    # list_export_fields = ('id', 'name', 'title')   #设置数据导出选项
    model_icon = 'fa fa-envelope'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
xadmin.site.register(StudentUser, StudentUserXadmin)
#注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
#注册全局样式的类
xadmin.site.register(views.CommAdminView, CommXadminSetting)