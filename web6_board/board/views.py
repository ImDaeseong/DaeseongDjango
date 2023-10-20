from .models import Board
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator


def delete(request, number):
    if request.method != 'POST':
        return render(request, 'board/deletepage.html', {"number": number})
    else:
        board = Board.objects.get(number=number)
        pwd = request.POST["pwd"]

        if pwd != board.pwd:
            context = {"msg": "비밀번호 오류", "url": "../../delete/" + str(number) + "/"}
            return render(request, "alert.html", context)

        try:
            board.delete()
            return HttpResponseRedirect("../../list/")
        except:
            context = {"msg": "삭제 오류", "url": "../../delete/" + str(number) + "/"}
            return render(request, "alert.html", context)


def detail(request, number):
    board = Board.objects.get(number=number)
    board.readcnt += 1
    board.save()
    return render(request, "board/detailpage.html", {"board": board})


def list(request):
    page = int(request.GET.get("page", 1))  # 페이지 번호
    all_board = Board.objects.all().order_by("-number")  # 모든 데이터 내림차순 정렬
    paginator = Paginator(all_board, 10)  # 목록 10개씩
    board_list = paginator.get_page(page)
    listcount = Board.objects.count()
    return render(request, "board/listpage.html", {"board": board_list, "listcount": listcount})


def update(request, number):
    if request.method != "POST":
        board = Board.objects.get(number=number)
        return render(request, 'board/updatepage.html', {'board': board})
    else:

        board = Board.objects.get(number=number)
        pwd = request.POST["pwd"]

        if board.pwd != pwd:
            context = {"msg": "비밀번호 오류", "url": "../../update/" + str(number) + "/"}
            return render(request, "alert.html", context)

        try:
            filename = request.FILES["filename2"].name
            file_upload(request.FILES["filename2"])
        except:
            filename = ""

        try:
            if filename == "":
                filename = request.POST["filename1"]
            name = request.POST["name"]
            sTitle = request.POST["sTitle"]
            sContent = request.POST["sContent"]
            dCreated = timezone.now()

            data = Board(
                number=number,
                pwd=pwd,
                name=name,
                sTitle=sTitle,
                sContent=sContent,
                dCreated=dCreated,
                filename=filename
            )
            data.save()
            return HttpResponseRedirect("../../list/")
        except Exception as e:
            context = {"msg": "업데이트 오류", "url": "../../update/" + str(number) + "/"}
            return render(request, "alert.html", context)


def file_upload(f):
    with open("media/images/" + f.name, "wb") as f1:
        for ch in f.chunks():
            f1.write(ch)


def write(request):
    if request.method != "POST":
        return render(request, "board/writepage.html")
    else:
        try:
            filename = request.FILES["filename"].name
            # print(filename)
            file_upload(request.FILES["filename"])
        except:
            filename = ""

        pwd = request.POST["pwd"]
        name = request.POST["name"]
        sTitle = request.POST["sTitle"]
        sContent = request.POST["sContent"]
        dCreated = timezone.now()
        readcnt = 0

        data = Board(
            pwd=pwd,
            name=name,
            sTitle=sTitle,
            sContent=sContent,
            dCreated=dCreated,
            readcnt=readcnt,
            filename=filename
        )
        data.save()

    return HttpResponseRedirect("../list/")
