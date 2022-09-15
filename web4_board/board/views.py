from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from board.models import board_content


def List_view(request):
    data_all = board_content.objects.all().order_by('-id')

    # 없으면 1로 지정
    cur_Page = int(request.GET.get('page', 1))
    if cur_Page < 0:
        cur_Page = 1

    # 한페이지 10개씩만 보이도록 설정
    page_range = 10
    paging = Paginator(data_all, page_range)
    page_data = paging.get_page(cur_Page)

    intStart = int((cur_Page - 1) / page_range) * page_range + 1
    intEnd = int(((cur_Page - 1) + page_range) / page_range) * page_range

    if paging.num_pages <= intEnd:
        intEnd = paging.num_pages

    # 총페이지
    total_page = paging.num_pages

    # 페이지 데이터
    pagelist = []
    i = intStart
    while i <= intEnd:
        pagelist.append(i)
        i += 1

    """
    for s in pagelist:
        print(str(s))
    """
    # print('cur_Page:' + str(cur_Page))
    # print('page_range:' + str(page_range))
    # print('intStart:' + str(intStart))
    # print('intEnd:' + str(intEnd))
    # print('total_page:' + str(total_page))

    # print('개수:' + str(paging.count))
    # print('페이지수:' + str(paging.num_pages))
    # print('1번 페이지:' + str(paging.get_page(1)))
    # print('페이지당 보여줄 개수:' + str(paging.per_page))
    # print('페이지 범위:' + str(paging.page_range))

    context = {
        'data': page_data,
        'cur_Page': cur_Page,
        'page_range': page_range,
        'intStart': intStart,
        'intEnd': intEnd,
        'total_page': total_page,
        'pagelist': pagelist,
    }
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
