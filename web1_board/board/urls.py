from . import views
from django.urls import path

urlpatterns = [
    path('', views.List_view, name='List_view'),
    path('AddItem/', views.Add_view, name='Add_view'),
    path('DetailItem/<pk>/', views.Detail_view, name='Detail_view'),
    path('DeleteItem/<pk>/', views.Delete_view, name='Delete_view'),
    path('UpdateItem/<pk>/', views.Update_view, name='Update_view'),
]
