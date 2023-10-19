from .models import Member
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time


def adduser(request):
    if request.method != "POST":
        return render(request, "member/adduserpage.html")
    else:

        id = request.POST["id"]
        pwd = request.POST["pwd"]
        name = request.POST["name"]
        gender = request.POST["gender"]
        tel = request.POST["tel"]
        email = request.POST["email"]
        picture = request.POST["picture"]

        member = Member(
            id=id,
            pwd=pwd,
            name=name,
            gender=gender,
            tel=tel,
            email=email,
            picture=picture
        )
        member.save()
        return HttpResponseRedirect("../login/")


def changepwd(request):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../login/"}
        return render(request, "alert.html", context)

    if request.method != "POST":
        return render(request, "member/changepwdpage.html")
    else:
        member = Member.objects.get(id=login)
        if member.pwd == request.POST["pwd"]:
            member.pwd = request.POST["pwd1"]
            member.save()
            context = {"msg": "비밀번호 수정 완료", "url": "../login/"}
            return render(request, "alert.html", context)
            return HttpResponseRedirect("../main")
        else:
            context = {"msg": "비밀번호 수정 오류", "url": "../login/"}
            return render(request, "member/changepwdpage.html", context)


def delete(request):
    return render(request, "member/deletepage.html")


def detail(request, id):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../login/"}
        return render(request, "alert.html", context)

    member = Member.objects.get(id=id)
    return render(request, "member/detailpage.html", {"member": member})


def list(request):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../login/"}
        return render(request, "alert.html", context)

    if login != "test":
        context = {"msg": "관리자만 가능", "url": "../main/"}
        return render(request, "alert.html", context)

    all_member = Member.objects.all()
    return render(request, "member/listpage.html", {"member": all_member})


def login(request):
    if request.method != "POST":
        return render(request, "member/loginpage.html")
    else:
        id = request.POST["id"]
        pwd = request.POST["pwd"]

        try:
            member = Member.objects.get(id=id)
        except:
            context = {"msg": "아이디를 확인하세요."}
            return render(request, "alert.html", context)

        if member.pwd == pwd:
            request.session["login"] = id
            time.sleep(1)
            print("2:", request.session.session_key)
            return HttpResponseRedirect("../main")
        else:
            context = {"msg": "비밀번호를 확인하세요.", "url": "../login/"}
            return render(request, "alert.html", context)


def update(request, id):
    return render(request, "member/updatepage.html")


def logout(request):
    print(request.session.session_key)
    auth.logout(request)
    return HttpResponseRedirect("../login/")


def main(request):
    print(request.session.session_key)
    return render(request, 'member/mainpage.html')
