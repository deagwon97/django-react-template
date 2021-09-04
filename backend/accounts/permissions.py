from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOnly(BasePermission):
    # https://ssungkang.tistory.com/entry/Django-APIView%EC%97%90-permission-%EC%A7%80%EC%A0%95%ED%95%98%EA%B8%B0
    # 작성자만 접근
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            print("로그인한 유저")
            if request.user.is_staff == '1':
                # 관리자
                print("관리자")
                return True
            elif obj.__class__ == get_user_model():
                print("id 존재")
                return obj.id == request.user.id

            return obj.user_id == request.user.id
        else:
            return False

class IsOwnerOrReadOnly(BasePermission):
    # 작성자만 접근, 작성자가 아니면 Read만 가능
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_staff == '1':
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == request.user.id
            elif obj.user_id == request.user.id:
                return True
            # 값을 바꾸지 않는 안전한 method
            elif request.method in SAFE_METHODS:
                #사용자가 SAFE_METHODS를 사용하는지 확인
                return True
            else:
                return False
        else:
            return False