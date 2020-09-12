from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post2 import views

# Default Router 사용 x ==> API ROOT 없음.

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post2/', views.PostList.as_view()),
    # 127.0.0.1:8000/post/<pk> == DetailView
    path('post2/<int:pk>', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)