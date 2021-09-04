from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .mangers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

# User와 1대1 대응관계 테이블
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                    on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)
    # blank=True
    # 폼에서 비워둘 수 있음. 데이터베이스에는 ''이 저장됨.
    myInfo = models.CharField(max_length=150, blank=True, null=True)

# User가 생성되면 자동으로 Profile 생성
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# User가 수정되면 자동으로 Profile 수정
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()