from django.urls import path
from member import views

urlpatterns = [
    path("adduser/", views.adduser, name="adduser"),
    path("changepwd/", views.changepwd, name="changepwd"),
    path("delete/", views.delete, name="delete"),
    path("detail/", views.detail, name="detail"),
    path("list/", views.list, name="list"),
    path("login/", views.login, name="login"),
    path("update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
]
