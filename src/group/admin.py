from django.contrib import admin

from group.models import Group


class GroupsAdmin(admin.ModelAdmin):
    list_per_page = 300
    list_display = ['id', 'course', 'number_students_in_group', 'start_group', 'head', 'curator']
    fields = ['course', 'start_group', 'number_students_in_group', 'head', 'curator']
    list_select_related = ['head', 'curator']

    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related('head')


admin.site.register(Group, GroupsAdmin)
