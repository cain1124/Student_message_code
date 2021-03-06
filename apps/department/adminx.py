import xadmin
from .models import DepartmentInfo, MajorInfo, ClassInfo
from import_export import resources


class DepartmentInfoResource(resources.ModelResource):

    class Meta:
        model = DepartmentInfo
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录
        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id
        fields = ('id', 'name', 'desc',)
        # exclude = ()


#内联，添加时一起院系时一起添加专业
class MajorInfoInline(object):
    model = MajorInfo
    extar = 0


class ClassInfoInline(object):
    model = ClassInfo
    extar = 0


class DepartmentInfoXadmin(object):
    list_display = ['id', 'name', 'desc', 'student_num', 'add_time']
    # 要显示的字段列表

    ordering = ['id']
    # 按照id顺序排列，如果是倒序-id

    search_fields = ['name', 'desc']
    # 要搜索的字段

    list_filter = ['name', 'desc', 'add_time']
    # 要筛选的字段

    show_detail_fields = ['name', 'desc']
    # 要展示详情的字段

    list_editable = ['name', 'desc']
    # 列表可直接修改的字段

    list_per_page = 10
    # 分页

    model_icon = 'fa fa-building'
    # 配置模型图标，也可以在GlobalSetting里面配置

    import_export_args = {
        'import_resource_class': DepartmentInfoResource,
        # 'export_resource_class': DepartmentInfoResource,
    }
    # 配置导入按钮

    #删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


# class DepartmentInfoAdmin(object):
#     list_display = ['name', 'desc', 'student_num', 'add_time']
#     import_excel = True
#     inlines = [MajorInfoInline]
#     model_icon = 'fa fa-building'
#     # import_export_args = {'import_resource_class': DepartmentInfoResource, }
#     # #                       'export_resource_class': DepartmentInfoResource}
#
#     def post(self, request, *args, **kwargs):
#         if 'excel' in request.FILES:
#             pass
#         # 必须返回，不然报错（或者注释掉）
#         return super(DepartmentInfoAdmin, self).post(request, *args, **kwargs)


class MajorInfoXadmin(object):
    list_display = ['id', 'department', 'name', 'student_num', 'add_time']
    import_excel = True
    model_icon = 'fa fa-building-o'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


class ClassInfoXadmin(object):
    list_display = ['id', 'major', 'name', 'student_num', 'add_time']
    model_icon = 'fa fa-university'

    # 删除功能
    def has_delete_permission(self, *args, **kwargs):
        return True


xadmin.site.register(DepartmentInfo, DepartmentInfoXadmin)
xadmin.site.register(MajorInfo, MajorInfoXadmin)
xadmin.site.register(ClassInfo, ClassInfoXadmin)