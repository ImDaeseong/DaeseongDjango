from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, include

# rest framework
router = DefaultRouter()
router.register('getlist1', views.List_API_ViewSet1)
router.register('getlist2', views.List_API_ViewSet2)

urlpatterns = [
    path('', views.List_view, name='List_view'),
    path('AddItem/', views.Add_view, name='Add_view'),
    path('DetailItem/<pk>/', views.Detail_view, name='Detail_view'),
    path('DeleteItem/<pk>/', views.Delete_view, name='Delete_view'),
    path('Search_view/', views.Search_view, name='Search_view'),
    path('UpdateItem/<pk>/', views.Update_view, name='Update_view'),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
