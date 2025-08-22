from django.contrib import admin
from django.urls import path,include


urlpatterns = [
  p
    path("", include("blog.urls")),  
    path('admin/', admin.site.urls),
     
    
]
