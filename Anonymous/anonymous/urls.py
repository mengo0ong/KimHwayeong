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
from board.views import board, post_write, post_detail
from user.views import signin, signup, sign_out
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name="signin"),
    path("user/signup", signup, name="signup"),
    path("user/signout", sign_out, name="signout"),
    path("post/write", post_write, name="post_write"),
    path("post/<int:post_id>", post_detail, name="post_detail")

]

# 만약 settings가 개발중이라면 해당하는 upload라는 경로로 들어왔을 때 정적인 파일을 매칭해서 보여줘
# 정적파일 경로는 settings의 MEDIA_ROOT로 지정
if settings.DEBUG:
    urlpatterns += static('upload', document_root=settings.MEDIA_ROOT)