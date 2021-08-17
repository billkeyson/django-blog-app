from django.http import request
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import CommentModel,CategoryModel, PostModel
from .serializers import CommentSerializer, CreatePostSerializer, PostSerializer,CategorySerializer,PostImageSerializer
from rest_framework import mixins,viewsets,status
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.exceptions import ValidationError

class BasePostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    error_messgae =''
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            raise ValidationError(_(self.error_messgae))

class GetPostViewSet(
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.CreateModelMixin):

    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    authentication_classes = (TokenAuthentication,)

    @action(methods=['POST'],url_path='upload-image',detail=True)
    def upload_image(self,request,pk=None):
        "Upload image"
        post = self.get_object()
        # print("obe ",post)
        serializer  = self.get_serializer(post,data= request.data)
        if serializer.is_valid():
            # print('Print',serializer.data)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        print('Dafial')
        return Response(
                        serializer.errors,
                        status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        """Return the class to use for the serializer. Defaults to using self.serializer_class.
            You may want to override this if you need to provide different serializations depending on the incoming request."""
        print(self.action,' image')
        if self.action == 'upload_image':
            print("image-upload")
            return PostImageSerializer
        return self.serializer_class
    def get_queryset(self):
        print('is called',self.action)
        # print("serial class",self.get_object())
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