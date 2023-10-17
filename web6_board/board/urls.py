from django.urls import path
from board import views

urlpatterns = [
    path("delete/", views.delete, name="delete"),
    path("detail/", views.detail, name="detail"),
    path("list/", views.list, name="list"),
    path("update/", views.update, name="update"),
    path("write/", views.write, name="write"),
]
