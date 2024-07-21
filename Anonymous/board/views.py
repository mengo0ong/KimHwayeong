from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator

def board(request):
    # 게시글 리스트
    if request.method == "GET":
        # 해당 페이지를 받을 때 페이지 key값이 없으면 default로 1을 받음
        # 같은 원리로 default값을 받아야할 때에는 .get('name', 'value')
        page = request.GET.get('page', 1)
        post_set = Post.objects.all().order_by('-id')
        paginator = Paginator(post_set, 4)

        # post_set 초기화
        post_set = paginator.get_page(page)

        # 아래의 내용이 html에서 django 태그로 작동한다.
        context = {
            "post_set": post_set

        }

        # Java의 Controller 같은 느낌
        return render(request, 'page/index.html', context=context)