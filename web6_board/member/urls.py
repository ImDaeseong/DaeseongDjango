from django.urls import path
from member import views

urlpatterns = [
    path("adduser/", views.adduser, name="adduser"),
    path("changepwd/", views.changepwd, name="changepwd"),
    path("delete/<str:id>/", views.delete, name="delete"),
    path("detail/<str:id>/", views.detail, name="detail"),
    path("list/", views.list, name="list"),
    path("login/", views.login, name="login"),
    path("update/<str:id>/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
    path("main/", views.main, name="logout"),
]
