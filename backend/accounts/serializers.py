from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from .models import Profile

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh_token'])
        data = {'access_token': str(refresh.access_token)}

        return data


class CustomRegisterSerializer(RegisterSerializer):
    """
    User와 Profile을 동시에 입력하기 위한 Sefilaizers
    """
    username = None
    nickname = serializers.CharField(required=False, max_length=64)
    myInfo = serializers.CharField(required=False, max_length=150, allow_null=True)
    photo = serializers.ImageField(required=False,  allow_null=True)

    def get_cleaned_data(self):
        # password, email이 디폴트
        data_dict = super().get_cleaned_data()
        # Profile에서 새롭게 추가한 
        # nickname, mygit, myInfo, photo를 새롭게 정의
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['myInfo'] = self.validated_data.get('myInfo', '')
        data_dict['photo'] = self.validated_data.get('photo', '')
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.profile.nickname = self.data.get('nickname')
        user.profile.myInfo = self.data.get('myInfo')
        user.profile.photo = self.data.get('photo')
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'id')

#profile 
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'user_id', 'photo',  'myInfo')