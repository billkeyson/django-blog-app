from django.http import request
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CommentModel,CategoryModel, PostModel
from .serializers import CommentSerializer, CreatePostSerializer, PostSerializer,CategorySerializer,PostImageSerializer
from rest_framework import mixins, serializers,viewsets,status
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from rest_framework.exceptions import ValidationError


class LatestPost(APIView):
    def get(self,request):
        latest_posts = PostModel.objects.all()[:3]
        serializer = PostSerializer(latest_posts,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class PostCaterogoies(APIView):
    def  get(self,request,post_id):
        category = CategoryModel.objects.filter(post_id = post_id).order_by('id')
        if category:
            serializer = CategorySerializer(category,many=True)
            return Response(serializer.data,status.HTTP_200_OK)
        return Response([],status.HTTP_200_OK)

class CategoryListCreate(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-post_id')


class BasePostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            raise ValidationError(_("Ops only admin can do this"))

class GetAndPostPostViewSet(
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.CreateModelMixin):

    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

   
    # def get_permissions(self):
    #     # check permission if is a create req
    #     if self.action =='create' or self.action == 'update' or self.action == 'delete':
    #         self.permission_classes = [IsAuthenticated,]
    #     return super().get_permissions()
    
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
        return Response(
                        serializer.errors,
                        status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        """Return the class to use for the serializer. Defaults to using self.serializer_class.
            You may want to override this if you need to provide different serializations depending on the incoming request."""
        if self.action == 'upload_image':
            return PostImageSerializer
        return self.serializer_class
    def get_queryset(self):
        return self.queryset.order_by('-created_at')
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # if self.request.user and self.request.user.is_superuser:
        #     serializer.save(user=self.request.user)
        # else:
        #     raise ValidationError('Ohps sorry your are not admin :)')

        # create new post
        return super().perform_create(serializer)
    
class DefaultView(object):
    def get(self, request,post_id=None,cat_id=None , format=None):

        # comments =CommentModel.objects.filter(post_id=post_id)
        # serializer = CommentSerializer(posts, many=True)

        posts = PostModel.objects.filter(pk=post_id)
        serializer = PostSerializer(posts, many=True)

        
        return Response(serializer.data)

class GetPostCommentDetailed(APIView,DefaultView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

class CreateAndViewCommentViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin):

    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(published=True)
    
    def perform_create(self, serializer):
        # PostModel.get()
        # print(serializer)
        # serializer.save(post_id=)
        return super().perform_create(serializer)
