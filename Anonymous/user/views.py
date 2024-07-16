from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from user.models import User

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']



def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')