from django.contrib import admin
from django.urls import path, include
from post2 import urls
from userpost import urls
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post2/', include('post2.urls')),
    path('userpost/', include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),

]