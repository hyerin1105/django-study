<< 14. Authentication >>

1) Authentication & Permission
    동작 원리: CRUD
    운영 원리: Authentication & Permission
    -> 제3자에게 관리자와 같은 권한을 주지 않게 하기 위함.
        - Authentication
          : 서비스를 이용하는 데에 있어 내가 어느 정도의 권한이 있음을 알려주는(요청하는) 과정
        - Permission
          : 서비스를 어느 정도로 이용할 수 있는지에 대한 권한

2) TokenAuthentication
    : 사용자가 인증 요청을 보냈을 때 관리자가 유일한 Key값을 보냄. (Token 헤더)

3) SesstionAuthentication
    : 로그인이 될 때마다 저장되는 Session 정보를 참조하여 인증

4) RemoteUserAuthentication
    : User 정보가 다른 서비스에서 관리될 때 쓰이는 인증 방식

* --auth username.password : ++유저로서 어떤 내용을 어떻게 보낼 것이다.

<< 15. Permission >>
    -> View 호출 시 가장 먼저 체킹
    -> 인증 정보(request.user, request.auth)를 기반으로 권한 체크

1) Permission 설정
    1. settings.py 전역 설정
        REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES' ; [
        'rest_framework.permission.IsAuthenticated',
        ]}
        <!-- IsAuthenticated => permission class -->
    2. view마다 설정
        from rest_framework.permissions import IsAuthenticateOrReadOnly, IsAdminUser ...

        class UserPostViewSet(viewsets.ModelViewSet):
            '''
            permission_classes = [IsAuthenticaticatedOrReadOnly]
            '''
        <!-- IsAuthenticateOrReadOnly, IsAdminUser => permission class -->
    3. FBV decorator를 이용한 설정(views.py)
        from rest_framework.permissions import IsAuthenticated

        @api_view(['GET'])
        @permission_classes([IsAuthenticated])
        def example_view(request, format=None):
        '''

2) Permission class 종류
    AllowAny(default): 인증된 요청이든 비인증 요청이든 전부 허용함
    IsAuthenticated: 인증된 요청에 대해서만 View 호출을 허용함.
                    (등록된 사용자에게만 Access 허용)
    IsAdminUser: Staff User에 대해서만 요청을 허용
                (User.is_staff == True일 때만 허용)
    IsAuthenticatedOrReadOnly: 비인증요청에 대해서는 읽기만 허용
                                (비인증요청은 '안전한 http method'만 허용)
    <!-- etc
    - DjangoModelPermissions
    - DjangoModelPermissionsOrAnonReadOnly
    - DjangoObjectPermissions -->

<< 16. Token 인증 >>

1) Token Authentication
    -> BasicAuthentication, SessionAuthentication의 한계
    -> Mobile Client에 적합
    
    1. Token Authentication 수행과정
        1️⃣ username. password와 1:1 매칭되는 고유 key 생성, 발급
            (User instance의 생성에 따라 자동으로 생성되는 건 아님)
            (1) rest_framework/authtoken/views.py의 ObtainAuthToken을 이용한 생성
            (2) Python 명령어를 통한 생성
        2️⃣ 발급받은 Token을 API 요청에 담아 인증처리
            인증 성공 시:
                request.user = Django User Instance
                request.auth = rest_framework.authtoken.models.BasicToken
        3️⃣ 
        4️⃣ 
        5️⃣ 
        6️⃣ 

2) Token Authentication 설정
    -> settings.py/
            INSTALLED_APPS = [
            ...
            'rest_framework',
            'rest_framework.authtoken'
            ...
            ]
        $ python manage.py migrate
        => authtoken/models.py의 OneToOneField를 이용해 Token을 발급할 것이기 때문

    * token을 생성하려면 터미널에 -> python manage.py drf_create_token <계정명(아이디)>

3) Token Authentication 획득
    생성한 Token의 획득:
        token을 획득할 수 있는 url path 지정
        -> 그 url에 대해 POST 요청을 보냄으로써 획득
        
        from rest_framework.authtoken.views import obtain_auth_token

        urlpatterns = [
            path('api-auth/', include('rest_framework.urls')),
            path('api-token-auth/', obtain_auth_token),
        ]