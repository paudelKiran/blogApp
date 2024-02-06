from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from django.conf import settings
from datetime import datetime
from .managers import CustomUserManager
from tinymce.models import HTMLField
from django.utils.html import format_html

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False)
    date_created = models.DateTimeField(default=datetime.now(), blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.email)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, default='')
    email_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    user_img = models.ImageField(upload_to="userImage/")
    



class Categories(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title= models.CharField(null= False, max_length=100,unique=True)
    desc= models.CharField(max_length=200,default="")
    url= models.CharField(null=False, max_length=100)
    image=models.ImageField(upload_to="category/")
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def img_viewer(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%"/>'.format(self.image))
    

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title= models.CharField(null= False, max_length=200)
    desc= HTMLField()
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    url= models.CharField(null=False, max_length=100)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="posts/",null=True)

    class Meta:
        verbose_name_plural="Posts"
    
    def __str__(self):
        return self.title
    
    def img_viewer(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%"/>'.format(self.image))
