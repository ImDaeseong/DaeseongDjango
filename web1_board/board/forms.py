from django import forms
from .models import board_content


class board_contentForm(forms.ModelForm):
    class Meta:
        model = board_content
        fields = ['sTitle', 'sContent', 'iImage']
