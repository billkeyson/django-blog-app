# from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import CommentModel,CategoryModel, PostModel
from .serializers import CommentSerializer, CreatePostSerializer, PostSerializer,CategorySerializer
from rest_framework import mixins,viewsets
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.exceptions import ValidationError


class GetPostViewSet(
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.CreateModelMixin):

    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    authentication_classes = (TokenAuthentication,)


    def get_queryset(self):
        print('is called')
        return self.queryset.filter(user=self.request.user).order_by('created_at')
    
    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            raise ValidationError('Ohps sorry your are not admin :)')

        # create new post
        return super().perform_create(serializer)

class CreatePostVieSet(mixins.CreateModelMixin):
    serializer_class = CreatePostSerializer
        



class CommentViewSet(ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def create(self,request):
        print(request)

class CategoryViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def create(self,request):
        print(request)
    def list(self,request):
        print(request, "lst")