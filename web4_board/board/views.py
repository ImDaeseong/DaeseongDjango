from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from board.models import board_content


def List_view(request):
    data_all = board_content.objects.all().order_by('-id')

    # 없으면 1로 지정
    page = int(request.GET.get('page', 1))

    # 한페이지 2개씩만 보이도록 설정
    paging = Paginator(data_all, 2)
    page_data = paging.get_page(page)

    context = {'data': page_data}
    return render(request, 'listPage.html', context)


def Detail_view(request, pk):
    data_all = board_content.objects.get(id=pk)
    # print(data_all.sTitle)
    # print(data_all.sContent)
    # print(data_all.iImage)
    context = {'data': data_all}
    return render(request, 'DetailPage.html', context)


def Add_view(request):
    if request.method == 'POST':
        sTitle = request.POST['sTitle']
        sContent = request.POST['sContent']

        if len(sTitle) == 0:
            return redirect('/AddItem/')

        if len(sContent) == 0:
            return redirect('/AddItem/')

        if len(request.FILES) != 0:
            iImage = request.FILES['iImage']
        else:
            iImage = None

        data = board_content(
            sTitle=sTitle,
            sContent=sContent,
            iImage=iImage
        )
        data.save()
        return redirect('/')
    return render(request, 'CreatePage.html')


def Update_view(request, pk):
    if request.method == "POST":
        sTitle = request.POST.get('sTitle')
        sContent = request.POST.get('sContent')

        if len(request.FILES) != 0:
            iImage = request.FILES.get('iImage')
        else:
            iImage = None

        data = board_content.objects.get(id=pk)
        data.sTitle = sTitle
        data.sContent = sContent

        if iImage is not None:
            if data.iImage:
                data.iImage.delete()
            data.iImage = iImage

        data.save()
        return redirect('/DetailItem/' + str(pk))

    item = board_content.objects.get(id=pk)
    context = {'data': item}
    return render(request, 'UpdatePage.html', context)


def Delete_view(request, pk):
    data_all = board_content.objects.get(id=pk)
    if data_all.iImage:
        data_all.iImage.delete()  # print(data_all.iImage)
    data_all.delete()
    return redirect('/')
