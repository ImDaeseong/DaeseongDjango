from django.shortcuts import render, redirect
from board.forms import board_contentForm
from board.models import board_content


def List_view(request):
    data_all = board_content.objects.all()
    # print(data_all)
    context = {'data': data_all}
    return render(request, 'listPage.html', context)


def Detail_view(request, pk):
    data_all = board_content.objects.get(id=pk)
    # print(data_all)
    context = {'data': data_all}
    return render(request, 'DetailPage.html', context)


def Add_view(request):
    form = board_contentForm()
    if request.method == "POST":
        form = board_contentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form_data': form}
    return render(request, 'CreatePage.html', context)


def Delete_view(request, pk):
    data_all = board_content.objects.get(id=pk)
    data_all.delete()
    return redirect("/")


def Update_view(request, pk):
    data_all = board_content.objects.get(id=pk)
    form = board_contentForm(instance=data_all)

    if request.method == "POST":
        form = board_contentForm(request.POST, instance=data_all)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form_data': form}
    return render(request, 'UpdatePage.html', context)
