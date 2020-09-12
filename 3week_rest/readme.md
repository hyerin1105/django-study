<< 8. mixins >>

1) SnippetList
    -> models.py에서 정의한 Snippet이라는 모델을 가져와서 객체들의 모든 목록을 띄워주는 ListView의 역할을 함.
        => 불필요한 코드 작성을 줄임.(상속을 통해서)

* 가변인자( , *args, **kwargs)
    : 받은 인자의 개수의 무관한 인자

<< 9. generic CBV >>


<< 10. ViewSet >>

1) Viewsets
    1. ReadOnlyModeViewSet
        : "class ReadOnlyModeViewSet():"에서 () 안에 있는 인자를 묶어주는 역할
        -> list()와 retrieve() 메소드는 묶어주는 역할

        if) 읽기 기능만 수행하는 view가 필요하면
            : ReadOnlyModel을 상속해서 ViewSet 만들고 queryset, serializer_class만 등록하면 읽기 기능만 수행할 수 있음.
    
    2. ModelViewSet
        : list(), create(), retrieve(), update(), partial_update(), destroy()를 묶어주는 역할
        (액션 데코레이터를 이용해 어떤 메소드를 사용하고, 어떤 모델로 할 것인지 등록해야 함.)

        * permission_classes = [permissions.IsAuthenticateOrReadOnly, IsOwnerOrReadOnly]
            => 권한 설정(인증 되면 권한을 주고, 미인증인 경우 읽기 권한만 줌.)

        * @ + 함수들 -> decorator, 장식자
        -> 내가 임의로 View를 설계할 때 => @action() = action decorator
        : 내가 임의로 View를 만들었으니 직접 Response를 만들어 보내야함.
            =>> Custom API의 Default Method는 GET이지만, action의 format 인자로 지정 가능.
    
    ==> ViewSet은 하나의 path 함수만으로 ListView, DetailView의 CRUD 처리 불가

<< 11. Router >>

1) Path()
    Path()를 묶어준다 == Path()의 두번째인자(로 오는 함수)를 묶는다.
    예) path(요청을 처리할 url, 요청을 인자로 받아 처리할 함수, namespace)
        -> 두번째 인자로 올 함수들 예) list(), create(), retrieve() ...

    ==> path()를 묶어주는 .as_view()
    예) as_view({'http_method' : '처리할_함수' })

<< 12. pagination >>

<< 13. filtering and search >>