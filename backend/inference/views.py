# Create your views here.

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .models import Inference
from .serializers import InferenceSerializer


# api/inference 으로 get하면 이 listview로 연결
class InferenceView(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Inference.objects.all()
    serializer_class = InferenceSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)