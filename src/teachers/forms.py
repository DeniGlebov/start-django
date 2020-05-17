from django import forms

from teachers.models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'course',
            'phone'
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        if phone != cleaned_phone:
            raise forms.ValidationError("Phone field only numbers!")
        return cleaned_phone
