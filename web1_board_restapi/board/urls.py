from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import List_API_1, List_API_2

urlpatterns = [
    path('', views.List_view, name='List_view'),
    path('AddItem/', views.Add_view, name='Add_view'),
    path('DetailItem/<pk>/', views.Detail_view, name='Detail_view'),
    path('DeleteItem/<pk>/', views.Delete_view, name='Delete_view'),
    path('Search_view/', views.Search_view, name='Search_view'),
    path('UpdateItem/<pk>/', views.Update_view, name='Update_view'),
    path('api/getlist1', List_API_1.as_view()),  # rest framework API 1
    path('api/getlist2', List_API_2.as_view()),  # rest framework API 2
    path('api/getlist3', views.List_API_3),  # rest framework API 3
    path('api/getlist4', views.List_API_4),  # rest framework API 4
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
