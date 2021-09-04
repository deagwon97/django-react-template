from __future__ import unicode_literals
from django.db import models
#from django.utils import timezone
from accounts.models import User

    
# 계산 객체 생성
class Inference(models.Model):
    author = models.ForeignKey(User, 
                                null = True, # DB에 null 저장을 허용(탈퇴 퇴출 등).
                                blank= False, # 입력 창에서는 반드시 author가 존재해야함.
                                on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    memo = models.TextField(blank = True, null = True)

    input_data = models.FileField(upload_to='list/files/%Y/%m/%d/', blank = True)

    output_data = models.FileField(upload_to='list/files/%Y/%m/%d/', blank = True, null = True)

    output_text = models.CharField(max_length=200,
                                        blank = True,
                                        null = True)

    thumbnail = models.ImageField(u'썸네일', 
                        upload_to='%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'