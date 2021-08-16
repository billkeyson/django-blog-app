from django.db import models
from django.contrib.auth import get_user_model


class PostModel(models.Model):
    user = models.ForeignKey(get_user_model(),help_text='author information',related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug =  models.SlugField(max_length=200)
    sammary  = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    

