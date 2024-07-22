from django.shortcuts import render, redirect
from board.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
import uuid

def board(request):
    # 게시글 리스트
    if request.method == "GET":
        # 해당 페이지를 받을 때 페이지 key값이 없으면 default로 1을 받음
        # 같은 원리로 default값을 받아야할 때에는 .get('name', 'value')
        page = request.GET.get('page', 1)
        # 검색
        search_text = request.GET.get('search_text', "")

        post_set = Post.objects.filter(
                # i는 대소문자를 가리지 않겠다는 의미, 없어도 됨
                title__icontains = search_text
            ).order_by('-id')
        paginator = Paginator(post_set, 4)

        # post_set 초기화
        post_set = paginator.get_page(page)



        # 아래의 내용이 html에서 django 태그로 작동한다.
        context = {
            "post_set": post_set,
            "search_text": search_text

        }

        # Java의 Controller 같은 느낌
        return render(request, 'page/index.html', context=context)

# 로그인 한 유저만 접근이 가능하도록 함
@login_required(login_url="signin")  
def post_write(request):
    if request.method=="GET":
        return render(request, "page/post_write.html")
    if request.method=="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        img = request.FILES.get("img", None)
        # 이미지가 들어오지 않았을 때의 초기화
        img_url = ""

        if img:
            """
            이미지 저장 
            - 이미지를 저장할 수 있는 Default folder 필요
            - Django 설정 -> settings.py -> static_url 아래에 MEDIA_ROOT='경로' 
            -> views.py 상단에 from django.core.files.storage import default_storage 
            """

            # 동일한 파일 이름이 들어왔을 때, 오류가 생기는 것을 방지하기 위해
            # 파일 이름을 고유하게 지정하기 위해 uuid 사용
            img_name = uuid.uuid4()
            # split으로 나눈 배열의 가장 마지막 값
            img_type = img.name.split('.')[-1]
            default_storage.save(f"{img_name}.{img_type}", img)
            img_url = f"{img_name}.{img_type}"

        # Post 객체 저장
        Post(
            user = request.user,
            title = title,
            content = content,
            img_url = img_url
        ).save()
        return redirect('board')
