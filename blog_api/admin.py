from django.contrib import admin
from blog_api import models

admin.site.register(models.PostModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.CommentModel)
