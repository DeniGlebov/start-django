from django import forms

from group.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'course',
            'number_students_in_group',
            'start_group',
        )
