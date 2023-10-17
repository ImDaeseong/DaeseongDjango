from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


def adduser(request):
    return render(request, "member/adduserpage.html")


def changepwd(request):
    return render(request, "member/changepwdpage.html")


def delete(request):
    return render(request, "member/deletepage.html")


def detail(request):
    return render(request, "member/detailpage.html")


def list(request):
    return render(request, "member/listpage.html")


def login(request):
    return render(request, "member/loginpage.html")


def update(request):
    return render(request, "member/updatepage.html")


def logout(request):
    print(request.session.session_key)
    auth.logout(request)
    return HttpResponseRedirect("../login/")
