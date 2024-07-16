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