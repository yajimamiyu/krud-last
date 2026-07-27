from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            'application_type',
            'title',
            'content',
        ]

        labels = {
            'application_type': '申請種類',
            'title': '件名',
            'content': '内容',
        }