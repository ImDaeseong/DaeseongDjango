from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("member/", include("member.urls")),
    path("board/", include("board.urls")),
]

#파일 업로드 위치 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)