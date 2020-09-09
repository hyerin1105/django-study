<< 4. REST Framework >>

1) REST란?
    REpresentational: 자원을 대표하는 단어/식별자료
    State Transfer: 자원의 상태를 전송하는 방법

    -> 자원을 이름으로 구분하여 상태를 전송하는 방법
    - 자원: 해당 소프트웨어가 관리하는 모든 것
            (문서, 그림, 데이터 등..) 
    - 이름: 자원을 표현하기 위한 이름
        (DB의 학생정보가 자원일 때, 이름은 students)
    - 상태: 데이터가 요청되어질 시점에서의 자원의 상태
        (json이나 xml로 데이터를 주고 받음.)

2) REST 설계 방법(장점)
    -> 하위 호환을 깨뜨리지 않고 독립적 발전

    REST의 구성 요소
    - 자원: URL
            (모든 자원은 고유한 ID가 존재, 예:'/groups/:group_id)
    - 행위: HTTP Method
            (GET, POST, PUT, DELETE)
    - 표현: json, xml, text 등...

    REST 설계 조건(= REST가 되기 위한 필요충분조건)
    1. Server - Client
    2. STATELESS
    3. Cache
    4. Uniform lnterface
    5. Layered System 
    6. Code-On-Demand

3) API
    Application Program Lnterface: Request, Response로 오가는 구조화된 데이터
    (= 사용하기 편하게 기능을 제공해주는 것)

    예) Client: 식당손님
        API: 웨이터(-> 서버와 클라이언트 사이의 메신저)
        Server: 요리사

4) REST API
    : REST 아키텍쳐 스타일을 따르는 API
    -> HTTP(GET, POST 등)로 CRUD를 구현할 수 있는 API
    (= REST 설계 조건을 잘 따르는 API)


<< 5-1. JSON 직렬화 - Serializer >>

1) Form vs Serializer
    1. Form --> django
        : Client(모델로부터) Field 생성
          전송 가능 형식(HTML Form)으로 만듦
          유효성 검사

    2. Serializer --> django REST framework
        : Client(모델로부터) Field 생성
          전송 가능 형식(JSON 문자열)으로 만듦
          유효성 검사

<< 6. View of DRF >>

1) ViewSet
    : View(CRUD)를 설계하는 쉽고 간단한 방법

<< 7. APIView >>
- APIView를 상속해 View를 설계할 땐 status와 Response를 import해 직접 응답 과정을 만듦.