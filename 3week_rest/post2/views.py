# 데이터 처리 대상 : 모델, Serializer import 시키기
from .models import Post2
from .serializer import PostSerializer

from rest_framework import generics
from rest_framework import mixins


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post2.objects.all() #쿼리셋 등록
    serializer_class = PostSerializer # Serializer 클래스 등록

    # get은 list 메소드를 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # post는 create를 내보내는 메소드
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostDetail(mixins.RetrievevModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post2.objects.all()
    serializer_class = PostSerializer
    
    # DetailView의 get은 retrieve을 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # put은 update를 내보내는 메소드
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # delete는 destroy를 내보내는 메소드
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#-------------------------------------------------------------------------------------------------------------------------

from post2.models import Post2
from post2.serializer import PostSerializer

from rest_framework import viewsets

# @action 처리
from rest_framework import rederers
from rest_framework.decorators import action
from django.http import HttpResponse

# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post2.objects.all()
    serializer_class = PostSerializer

'''
# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class PostViewSet(viewSets.ModelViewSet):
    queryset = Post2.objects.all()
    serializer_class = PostSerializer

    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")
'''