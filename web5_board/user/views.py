from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_password = request.POST.get('user_password')

        user = authenticate(request, username=user_id, password=user_password)
        if user is not None:
            auth.login(request, user)
            return redirect('List_view')
        else:
            return render(request, 'LoginPage.html', {'error': '로그인 정보 확인이 필요합니다.'})
    else:
        return render(request, 'LoginPage.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('List_view')
    return render(request, 'LoginPage.html')


def addUser(request):
    if request.method == 'POST':
        if request.POST['user_password1'] == request.POST['user_password2']:
            user = User.objects.create_user(username=request.POST['user_id'], password=request.POST['user_password1'])
            auth.login(request, user)
            return redirect('List_view')
    return render(request, 'AddUserPage.html')