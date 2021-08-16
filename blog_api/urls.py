from django.urls import path,include
# from .views import GetPostView,PostViewSetList
from .api_views import GetPostViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register('', GetPostViewSet)

urlpatterns = [
    path('',include(router.urls)),
    ]