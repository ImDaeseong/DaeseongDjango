from rest_framework.serializers import ModelSerializer

from board.models import board_content


class boardSerializerAll(ModelSerializer):
    class Meta:
        model = board_content
        fields = '__all__'


class boardSerializer(ModelSerializer):
    class Meta:
        model = board_content
        fields = ['sTitle', 'sContent', 'iImage']