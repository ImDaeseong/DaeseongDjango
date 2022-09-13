from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_password = request.POST['user_password']
        user_email = request.POST['user_email']

        user = authenticate(request, username=user_id, password=user_password, email=user_email)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'LoginPage.html', {'error': '로그인 정보 확인이 필요합니다.'})
    else:
        return render(request, 'LoginPage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def addUser(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_password1 = request.POST['user_password1']
        user_email = request.POST['user_email']

        if User.objects.filter(username=user_id).exists():
            return render(request, 'AddUserPage.html', {'error': "이미 존재하는 사용자입니다."})

        if user_password1 == request.POST['user_password2']:
            user = User.objects.create_user(username=user_id, password=user_password1, email=user_email)
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'AddUserPage.html', {'error': "비밀번호가 일치하지 않습니다."})
    else:
        return render(request, 'AddUserPage.html')
