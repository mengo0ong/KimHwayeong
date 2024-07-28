from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# AbstractUser (상속받은 테이블)
# -django 기본 유지 모델
# 각종 필드, 함수(유저 생성, 인증 등등)..이 포함되어 있음.
class User(AbstractUser):
    # 닉네임 30글자 제한 커스텀
    nickname = models.CharField(max_length=30)

    # table name user
    class Meta:
        db_table="user"

# AbstractBaseUser
# -django 최소 유저 모델
# (필드: 비밀번호, 마지막로그인, 활성여부 3가지만 존재, 최소한의 함수만 존재)
# 따라서, 로그인시 필요한 필드 등 많은 부분이 커스텀가능
# 하지만, 장고의 유저 관련 함수들을 직접 정의해야하는 번거로움이 있다.
