import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model

def post_image_file_path(instance,filename):

    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(f'upload{os.sep}posts{os.sep}',filename)
    # return f'.\\upload/posts\\{filename}'

class PostModel(models.Model):
    user = models.ForeignKey(get_user_model(),help_text='author information',related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug =  models.SlugField(max_length=200)
    sammary  = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    image = models.ImageField(null=True,upload_to=post_image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def user_id(self):
        return self.user

    def email(self):
        return self.user.email
    
    def commants(self):
        return CommentModel.objects.filter(post_id=self.id)

    def total_comments(self):
        return CommentModel.objects.filter(post_id=self.id).count()
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title
    
class CommentModel(models.Model):
    post_id = models.ForeignKey(PostModel,related_name='comments',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['created_at']
    def __str__(self):
        return self.title

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    post_id = models.ForeignKey(PostModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

