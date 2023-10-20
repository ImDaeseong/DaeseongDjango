from django.db import models

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

# User 테이블에서 디폴트로 제공하는 컬럼 항목
"""
username: 사용자의 고유한 사용자 이름 (username)을 나타내는 문자열 필드입니다.
password: 사용자의 비밀번호를 나타내는 필드입니다. 비밀번호는 보안상 해싱된 형태로 저장됩니다.
email: 사용자의 이메일 주소를 나타내는 문자열 필드입니다.
first_name: 사용자의 이름의 첫 부분 (이름)을 나타내는 문자열 필드입니다.
last_name: 사용자의 이름의 뒷 부분 (성)을 나타내는 문자열 필드입니다.
is_active: 사용자 계정의 활성/비활성 상태를 나타내는 부울 필드입니다.
is_staff: 사용자가 관리자(Admin) 권한을 가지는지 여부를 나타내는 부울 필드입니다.
is_superuser: 사용자가 슈퍼유저(관리자의 최상위 권한)인지 여부를 나타내는 부울 필드입니다.
date_joined: 사용자가 가입한 날짜와 시간을 저장하는 필드입니다.
"""


class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    profile = models.CharField(max_length=200)

    def __str__(self):
        return self.id + ":" + self.name + ":" + self.pwd
