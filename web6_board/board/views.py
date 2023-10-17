from django.shortcuts import render


def delete(request):
    return render(request, "board/deletepage.html")


def detail(request):
    return render(request, "board/detailpage.html")


def list(request):
    return render(request, "board/listpage.html")


def update(request):
    return render(request, "board/updatepage.html")


def write(request):
    return render(request, "board/writepage.html")
