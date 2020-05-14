from django.contrib import admin

from group.models import Group


class GroupsAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'course', 'number_students_in_group', 'start_group')
    fields = ('course', 'start_group', 'number_students_in_group')


admin.site.register(Group, GroupsAdmin)
