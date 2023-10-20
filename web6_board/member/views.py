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
        profile = request.POST["profile"]
        member = Member(
            id=id,
            pwd=pwd,
            name=name,
            gender=gender,
            tel=tel,
            email=email,
            profile=profile
        )
        member.save()
        return HttpResponseRedirect("../login/")


def file_upload(f):
    with open("media/profile/" + f.name, "wb") as f1:
        for ch in f.chunks():
            f1.write(ch)


def profile(request):
    if request.method != "POST":
        return render(request, "member/profileimagepage.html")
    else:
        profile = request.FILES["profile"].name
        file_upload(request.FILES["profile"])
        return render(request, "member/profilepage.html", {"profile": profile})


def delete(request, id):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../../login/"}
        return render(request, "alert.html", context)

    if login == id:
        return delete_confirm(request, id)
    else:
        context = {"msg": "본인만 삭제 가능합니다.", "url": "../../login/"}
        return render(request, "alert.html", context)


def delete_confirm(request, id):
    if request.method != "POST":
        return render(request, "member/deletepage.html", {"id": id})
    else:
        login = request.session["login"]
        member = Member.objects.get(id=login)
        if member.pwd == request.POST["pwd"]:
            m = Member.objects.get(id=id)
            m.delete()
            if id == login:
                auth.logout(request)
                context = {"msg": "탈퇴완료", "url": "../../login/"}
                return render(request, "alert.html", context)
            else:
                return HttpResponseRedirect("../../list/")
        else:
            context = {"msg": "비밀번호가 일치하지 않습니다.", "url": "../../delete/" + id}
            return render(request, "alert.html", context)


def detail(request, id):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../../login/"}
        return render(request, "alert.html", context)

    member = Member.objects.get(id=id)
    return render(request, "member/detailpage.html", {"member": member})


def list(request):
    try:
        login = request.session["login"]
    except:
        context = {"msg": "로그인 하세요", "url": "../../login/"}
        return render(request, "alert.html", context)

    if login != "test":
        context = {"msg": "관리자만 가능", "url": "../../main/"}
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
            # print(request.session.session_key)
            return HttpResponseRedirect("../main")
        else:
            context = {"msg": "비밀번호를 확인하세요.", "url": "../../login/"}
            return render(request, "alert.html", context)


def logout(request):
    # print(request.session.session_key)
    auth.logout(request)
    return HttpResponseRedirect("../login/")


def main(request):
    return render(request, 'member/mainpage.html')
