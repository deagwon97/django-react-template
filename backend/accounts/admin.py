from django.contrib import admin

from .models import User
from .models import Profile
from django.contrib import admin
# from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from django.contrib.auth.admin import UserAdmin
class ProfileInline(admin.StackedInline): 
    # 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
    model = Profile
    con_delete = False                    # 프로필을 아예 없앨 수 없게 하는 속성(한번 만들면 지우는건 이상하니까)

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    ordering = ('email',)


admin.site.unregister(OutstandingToken)
admin.site.register(User, CustomUserAdmin)