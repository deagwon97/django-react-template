#backend/post/urls.py
from django.urls import path 
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Inference', views.InferenceView, 'Inference')

urlpatterns = [
    path('', include(router.urls))
]