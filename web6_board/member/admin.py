from django.contrib import admin
from .models import Member

# 관리자 페이지에서 Member 모델을 조작할 수 있는 인터페이스가 생성
admin.site.register(Member)