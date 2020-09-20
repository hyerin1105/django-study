from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permission import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter] # 어떤 것을 기반으로 서치필터를 적용할 것인지
    search_fields = () # 어떤 칼럼을 기반으로 검색할 것인지
                        # search_fields는 튜플이라 () 안에 ,를 꼭 넣어야 함. -> 예) ('title',)
 
    def get_queryset(self):
        # 여기 내부에서 쿼리셋을 실행한 후
        qs = super().get_queryset()

        # .filter .exclude
        # qs = qs.filter(author)

        # 만약 로그인이 되어 있지 않다면 -> 비어있는 쿼리셋을 리턴해라
        if self.request.user.is_authenticated:
            # 만약 지금 로그인이 되어 있다면 -> 로그인한 유저의 글만 필터링을 하려면
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
            # is_authenticated: 유저 인증이 되었는지 안 되었는지 확인하는 코드    

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)