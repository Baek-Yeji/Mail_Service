from django.db import models

# Create your models here.
class User(models.Model):
    # objects = models.Manager()
    user_id = models.CharField(max_length=20,verbose_name='아이디')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    user_name = models.CharField(max_length=10, verbose_name='사용자명')
    user_tel = models.CharField(max_length=15, verbose_name='전화번호')
    
    # 데이터가 문자열로 변환이 될 때 어떻게 나올지 정의하는 함수
    # def __str__(self):
    #     return self.user_name
    # 별도로 테이블명을 지정하고 싶을 때 쓰는 코드
    class Meta:
        db_table = 'users' # 테이블명
        verbose_name = "회원 정보" #노출된 테이블 이름 변경
        verbose_name_plural = "회원 정보" # 뒤에 자동으로 붙는 s를 대체해주기 위해
