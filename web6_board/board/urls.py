from django.urls import path
from board import views

urlpatterns = [
    path("delete/<int:number>/", views.delete, name="delete"),
    path("detail/<int:number>/", views.detail, name="detail"),
    path("list/", views.list, name="list"),
    path("update/<int:number>/", views.update, name="update"),
    path("write/", views.write, name="write"),
]
