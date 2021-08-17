from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models




class UserManagement(BaseUserManager):
    def create_user(self,email,password=None,username='', **extra_fields):
        """Create and save new user"""
        nor_email = self.normalize_email(email)
        user = self.model(email=nor_email,username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self,email,password):
        print('superuser')
        user = self.create_user(email=email,password=password)
        user.is_admin =True
        user.is_active =True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    """Customize user model"""
    email= models.EmailField(unique=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    username = models.CharField(max_length=50)
    
    objects = UserManagement()
    USERNAME_FIELD = 'email'