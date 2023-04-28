from django.db import models
import sys
import os

from myproject.utils import uuid_name_upload_to


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    
    # 필드 및 업로드 시간대별 다른 디렉토리에 저장
    # photo = models.ImageField(blank = True, upload_to='instagram/post/%Y/%m/%d')    
    
    # uuid를 통한 중복방지 파일명 지정
    photo = models.ImageField(blank = True, upload_to=uuid_name_upload_to, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name = "공개여부")
    
    # java의 tostring
    # 모델 커스텀
    # def __str__(self):
    #     return f"Custom Post object ({self.id})"
    

