from __future__ import absolute_import, unicode_literals
#https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

import os

from celery import Celery

# DJANGO_SETTINGS_MODULE의 환경 변수를 설정
# 자동으로 설정 모듈이 셀러리 프로그램으로 전달
# 문자열로 등록은 Celery Worker가 자식 프로세스에게 피클링하지 하지 않아도 되다고 알림
# namespace = 'CELERY'는 Celery관련 세팅 파일에서 변수 Prefix가 CELERY_ 라고 알림
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
# 결과를 받기 위해서는 backend를 필수로 설정
app = Celery('backend', backend='rpc://')
# Load task modules from all registered Django app configs.
# app 들 중에서 자동으로  celery가 자동적으로 tasks.py를 찾음.
app.config_from_object('django.conf:settings', namespace='CELERY')
# https://stackoverflow.com/questions/51795949/celery-4-2-django-recursionerror-maximum-recursion-depth-exceeded
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')