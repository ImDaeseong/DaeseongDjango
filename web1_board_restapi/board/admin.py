from django.contrib import admin
from board.models import board_content


# list_display 설정대로 id,sTitle,sContent,dCreated,dUpdated 보임
# @admin.register(board_content)
class board_content_Admin(admin.ModelAdmin):
    # Admin 목록에 보여질 필드 목록
    list_display = ('id', 'sTitle', 'sContent', 'dCreated', 'dUpdated')

    # 목록 내 링크 필드 목록
    list_display_liks = ['id', 'sTitle']


admin.site.register(board_content, board_content_Admin)
