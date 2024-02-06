from django.contrib import admin
from django.urls import path,include
from main.views import RegisterUser,verify,loginUser,getBlog,createBlog,updateBlog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/',RegisterUser.as_view()),
    path('api/login/',loginUser),
    path('api/getBlog/',getBlog.as_view()),
    path('api/createBlog/',createBlog.as_view()),
    path('api/updateBlog/<slug:pk>',updateBlog.as_view()),
    path( "verify/<slug:pk>/",verify.as_view()),
    path('tinymce/', include('tinymce.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
