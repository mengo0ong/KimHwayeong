from django.shortcuts import render

# Create your views here.
def board(request):
    if request.method == "GET":
        # 아래의 내용이 html에서 django 태그로 작동한다.
        context = {
            "title":"안녕 베어유?"
        }

        # Java의 Controller 같은 느낌
        return render(request, 'page/index.html', context=context)