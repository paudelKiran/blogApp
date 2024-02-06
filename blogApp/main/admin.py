from django.contrib import admin
from .models import User,Profile,Categories,Blog

class userAdmin(admin.ModelAdmin):
    list_display = ['email','date_created']

class profileAdmin(admin.ModelAdmin):
    list_editable = ['is_verified']
    list_display = ['user','full_name','email_token','is_verified']

class categoryAdmin(admin.ModelAdmin):
    list_display = ['img_viewer','title',"url","date"]

class blogAdmin(admin.ModelAdmin):
    list_display = ['img_viewer','title','category']
    list_filter=["category"]
   

admin.site.register(User,userAdmin)
admin.site.register(Profile,profileAdmin)
admin.site.register(Categories,categoryAdmin)
admin.site.register(Blog,blogAdmin)


