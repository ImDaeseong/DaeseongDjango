from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from board import views

urlpatterns = [
    path('AddItem/', views.Add_view, name='Add_view'),
    path('DetailItem/<pk>/', views.Detail_view, name='Detail_view'),
    path('DeleteItem/<pk>/', views.Delete_view, name='Delete_view'),
    path('Search_view/', views.Search_view, name='Search_view'),
    path('UpdateItem/<pk>/', views.Update_view, name='Update_view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)