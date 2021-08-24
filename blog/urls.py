from django.urls import path,re_path
from .views import index
urlpatterns = [
    # 127.0.0.1:8000 --> local
    # mydjangosite.com --> online
    re_path(r'^(?!api\/)(?!admin\/)[\/\w\.\,-]*', index, name='post_list'),
]