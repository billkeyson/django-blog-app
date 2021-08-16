from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import PostModel
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


class GetPostView(APIView):
    
    def get(self,request,format=None):
        print(request)
        post = PostModel.objects.get()
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def check_permissions(self, request):
        print('check permiisn')


class PostViewSetList(ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    """
    A viewset that provides the standard actions
    """
    @action(detail=False, methods=['post'])
    def create_posts(self, request):
        user = self.get_object()
        print(user)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():

            print(serializer.data)
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=401)

    @action(detail=False)
    def posts(self, request):
        all_posts =self.get_object()
        print(request,'gg')
        page = self.paginate_queryset(all_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_posts, many=True)
        return Response(serializer.data)

