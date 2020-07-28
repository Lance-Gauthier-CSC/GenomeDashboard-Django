from django import forms
from master.models import Session  # models.py


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            'file'
        ]