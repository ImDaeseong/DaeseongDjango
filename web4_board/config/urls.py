from django.contrib import admin
from django.urls import path, include

import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.List_view, name='List_view'),
    path('', include('board.urls')),
    path('', include('user.urls')),
]
