"""anonymous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from board.views import board, post_write
from user.views import signin, signup, sign_out

urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name="signin"),
    path("user/signup", signup, name="signup"),
    path("user/signout", sign_out, name="signout"),
    path("post/write", post_write, name="post_write")
]
