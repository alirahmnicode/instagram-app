from django.contrib import admin
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('users.urls')),
    path('comment/', include('comment.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)