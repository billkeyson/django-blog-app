from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog_api import models


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = models.PostModel
        fields = ('user','title','content','sammary','slug','published')
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = models.PostModel
        fields = ('id','user','title','content','sammary','slug','published','created_at')
        read_only_fields = ('user','created_at')
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        post_id = PostSerializer()
        model = models.CategoryModel
        fields = ('id','title','post_id')
   


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        post_id = PostSerializer()
        model = models.CommentModel
        fields = ('id','title','published','post_id','created_at','updated_at')
    
    