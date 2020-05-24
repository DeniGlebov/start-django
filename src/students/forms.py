from django import forms

from students.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'password',
            'phone',
        )

    def clean_phone(self):  # clean_ + field
        phone = self.cleaned_data['phone']
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        if phone != cleaned_phone:
            raise forms.ValidationError("Phone field only numbers!")
        return cleaned_phone

    # def clean(self):
    #     pass
    #
    # def save(self, commit=True):
    #     pass


class ContactUS(forms.ModelForm):
    class Meta:
        fields = (
            'title',
            'message',
            'email_from',
        )
