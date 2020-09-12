from rest_framework.routhers import DefaultRouter
from django.urls import include, path
from userpost import views

router = DefaultRouter()
router.register('', views.UserPostViewSet)

urlpatterns = [
    path('', include('router.urls')),
]