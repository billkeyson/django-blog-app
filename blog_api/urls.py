from django.urls import path,include
# from .views import GetPostView,PostViewSetList
from .api_views import (
                        GetAndPostPostViewSet,
                        CreateAndViewCommentViewSet,
                        GetPostCommentDetailed,LatestPost,
                        CategoryListCreate,PostCaterogoies )

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
app_name="blog_api"
router = routers.DefaultRouter()
router.register('', GetAndPostPostViewSet)
router.register('comments', CreateAndViewCommentViewSet)
router.register('category', CategoryListCreate)



urlpatterns = [
    path('',include(router.urls)),
    path('all/<int:post_id>/<int:cat_id>/',GetPostCommentDetailed.as_view()),
    path('latest/',LatestPost.as_view()),
    path('category/<int:post_id>/posts',PostCaterogoies.as_view())
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)