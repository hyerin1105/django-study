from rest_framework import viewsets
# 데이터 처리 대상
from .models import Post
from .serializer import PostSerializer
# status에 따라 직접 Response를 처리할 것
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
# APIView를 상속 받은 CBV
from rest_framework.views import APIView
# PostDetail 클래스의 get_object 메소드 대신 써도 됨.
# from django.shortcuts import get_object_or_404


class PostVeiwSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(APIView):
    def get(self, request):
        Posts = Post.objects.all()
        serializer = PostSerializer(Posts, many=True) # 쿼리셋 넘기기(many=True인자)
        return Response(serializer.data) # 직접 Response 리턴해주기 : serializer.data

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PostList 클래스와는 달리 pk값을 받음(메소드에 pk인자)
class PostDetail(APIView):
    # get_object_or_404를 구현해주는 helper function
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(Post)
        return Response(serializer.data)

    # 위 post 메소드와 비슷한 논리
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

