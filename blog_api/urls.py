from django.urls import path,include
# from .views import GetPostView,PostViewSetList
from .api_views import GetPostViewSet

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
router = routers.DefaultRouter()
router.register('', GetPostViewSet)

urlpatterns = [
    path('',include(router.urls)),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)