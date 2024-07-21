from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator

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
    
def post_write(request):
    if request.method=="GET":
        return render(request, "page/post_write.html")
