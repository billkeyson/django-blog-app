from .api_views import CreatePostViewSet,CreateTokenViewSet
from django.urls import path

app_name='user'

urlpatterns = [
    path('create/',CreatePostViewSet.as_view(),name='create'),
    path('token/',CreateTokenViewSet.as_view(),name='token')
    ]