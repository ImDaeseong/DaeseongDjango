from django.forms import ModelForm
from board.models import board_content


class board_contentForm(ModelForm):
    class Meta:
        model = board_content
        fields = ['sTitle', 'sContent']
