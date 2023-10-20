from django.urls import path
from member import views

urlpatterns = [
    path("adduser/", views.adduser, name="adduser"),
    path("delete/<str:id>/", views.delete, name="delete"),
    path("detail/<str:id>/", views.detail, name="detail"),
    path("list/", views.list, name="list"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("main/", views.main, name="main"),
    path("profile/", views.profile, name="profile"),
]
