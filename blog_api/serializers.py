from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog_api import models


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','username')

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = models.PostModel
        fields = ('user','title','content','comments','sammary','slug','published')
    
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        fields = ('id','image',)
        read_only_fields = ('id',)

class CommentInfor(serializers.ModelSerializer):
    class Meta:
        model = models.CommentModel
        fields = ('title','created_at')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        # fields= '__all__'
        fields = ('id','user','email','title','content','slug','total_comments','sammary','published','image','created_at')
        # exclude = ['slug']
        read_only_fields = ('user','created_at','id','total_comments')
    def get_title(self,obj):
        req = self.context('request')
        print(req)
        return 
class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentInfor(many=True)
    class Meta:
        # user = get_user_model()
        model = models.PostModel
        # fields= '__all__'
        fields = ('id','user','title','content','slug','comments','total_comments','sammary','published','image','created_at')
        # exclude = ['slug']
        read_only_fields = ('user','created_at','id','comments','total_comments')
    
    def validate(self, attrs):
        print(attrs,' validate')
        return super().validate(attrs)

    def validate_title(self, value):
        """
        Check that the blog post is about Sam.
        """
        if 'sam' not in value.lower():
            raise serializers.ValidationError("Blog post is not about sam")
        return value

    def create(self, validated_data):
        print(validated_data,' hecking')
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    post_id = PostSerializer()
    class Meta:
        model = models.CategoryModel
        fields = ('id','title','post_id',)
        read_only_fields = ('id',)

   


class CommentSerializer(serializers.ModelSerializer):
    # post_id = PostSerializer()
    class Meta:
        # post_id = PostSerializer(many=True)
        model = models.CommentModel
        fields = ('id','title','published','post_id','created_at','updated_at')
        read_only_fields = ('id',)

class  CategorySerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = ('title','post_id')  
    