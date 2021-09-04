from rest_framework import serializers
from .models import Inference
# 계산 시리얼 라이저. api 필드에서 보여줄 필드 명시
class InferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inference
        fields = '__all__'
