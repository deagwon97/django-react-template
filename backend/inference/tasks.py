from celery import shared_task
# from .models import Ranking, Category, Tag

from datetime import timedelta
from .models import *


@shared_task
def add(a, b):
    return a + b