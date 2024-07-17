from django.shortcuts import render, redirect
# Django rib auth (로그인, 로그아웃)
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Django message rib
from django.contrib import messages

# made User object
from user.models import User

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')
    if request.method == "POST":
        # POST로 받은 데이터
        username = request.POST['username']
        password = request.POST['password']

        # Django 내부적으로 User객체를 반환
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            messages.error(request, '입력값을 확인해 주세요.')
            return redirect('signin')



def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')
    
    if request.method =="POST":
        username = request.POST['username']
        nickname = request.POST['nickname']
        password = request.POST['password']

        # 이중가입 방지 check username
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, '동일한 아이디가 있습니다.')
            return redirect('signin')
        else:
            """
            password를 관리자ID로 DB상으로 다 볼 수 있기 때문에 암호화가 필요
            그렇기 때문에 make_password 메소드를 사용하여 django 내부적인 암호화 라이브러리 사용
            """
            new_user = User(
                username = username,
                password = make_password(password),
                nickname = nickname,
            )
            # 새로운 user정보를 저장
            new_user.save()
            login(request, new_user)
            return redirect('board')