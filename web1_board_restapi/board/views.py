from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from board.forms import board_contentForm
from board.models import board_content
from board.serializers import boardSerializerAll, boardSerializer, boardSerializerOne
from rest_framework.decorators import api_view


# rest framework API 1
class List_API_1(APIView):
    def get(self, request):
        queryset = board_content.objects.all()
        # print(queryset)
        serializer = boardSerializerAll(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return HttpResponse(status=200)


# rest framework API 2
class List_API_2(APIView):
    def get(self, request):
        queryset = board_content.objects.all()
        # print(queryset)
        serializer = boardSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return HttpResponse(status=200)


# rest framework API 3
@api_view(['GET'])
def List_API_3(request):
    queryset = board_content.objects.all()
    # print(queryset)
    serializer = boardSerializerOne(queryset, many=True)
    return Response(serializer.data)


# rest framework API 4
@api_view(['GET', 'POST'])
def List_API_4(request):
    if request.method == 'POST':
        return HttpResponse(status=200)
    queryset = board_content.objects.all()
    # print(queryset)
    serializer = boardSerializerOne(queryset, many=True)
    return Response(serializer.data)


def List_view(request):
    data_all = board_content.objects.all()
    # print(data_all)
    context = {'data': data_all}
    return render(request, 'listPage.html', context)


def Search_view(request):
    data_all = board_content.objects.all()
    search = request.GET.get('search', '')
    if search:
        search_list = data_all.filter(Q(sTitle__icontains=search))
        # print(search_list)
        context = {'data': search_list}
    else:
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
        form = board_contentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form_data': form}
    return render(request, 'CreatePage.html', context)


def Delete_view(request, pk):
    data_all = board_content.objects.get(id=pk)

    if data_all.iImage:
        data_all.iImage.delete()  # print(data_all.iImage)

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
