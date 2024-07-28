from django.db import models
from user.models import User

class Post(models.Model):
    # PK를 지정해주는 방법도 있지만, 아무런 값도 지정하지 않으면
    # Django 내부적으로 PK를 지정해준다.

    # 새로운 글이 테이블에 저장되면 로그인한 user가 글 쓴 것이라고 기본키로 지정
    # user가 삭제되면 글도 같이 삭제
    # null로 설정시 on_delete=models.SET_NULL, null=True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 해당 글이 들어오면 그 시간으로 값을 저장
    reg_date = models.DateTimeField(auto_now_add=True)
    # 빈 값이어도 됨을 설정
    img_url = models.URLField(null=True)

    class Meta:
        # 만약 테이블 이름을 지정하지 않으면 app_model (ex: board_post)
        db_table="post"


# FK -> Parents.children_set
# post.comment_set
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"