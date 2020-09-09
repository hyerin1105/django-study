<< 1. JSON >>
- JSON을 딕셔너리로 전송할 때: 문자열로 변환해서 전송

<< 2. Http Request & Response >>

1) GET과 POST의 차이
    GET: '갖다줘', URL 입력 데이터 뜸 (GET으로 전송할 때는 ==)
    POST: '처리해줘', URL 안 뜸 (POST/PUT으로 전송할 때는 =)

    예) http://127.0.0.1:8000/new
    GET: '빈 입력 공간을 갖다줘'
    POST: '지금 입력한 내용을 처리해줘'

2) 용어(Method) 정리
    GET: 요청받은 URL의 정보를 검색해 응답
    POST: 요청된 자원 생성(CREATE)
    PUT: 요청된 자원 수정(UPDATE)
    DELETE: 요청된 자원 삭제
    PATCH: 요청된 자원의 일부를 교체/수정
    OPTION: 웹서버에서 지원되는 메소드의 종류 확인

    예) http://likelion.net/post/1
    GET: '1번 글을 갖다줘'
    POST: (이미 만든 post/id는 POST 필요 없음)
    PUT, PATCH: '1번 글에 ~~한 내용을 --로 수정해줘'
    DELETE: '1번 글을 지워줘'

3) Http Response
    1. 1xx(정보): 요청을 받음, 프로세스 계속 진행
    2. 2xx(성공): 요청을 성공적으로 받음, 인식 -> 수용
    3. 3xx(리다이렉션): 요청 완료를 위해 추가 작업 조치 필요
    4. 4xx(클라이언트 오류): 요청의 문법이 잘못됐거나 요청 처리 불가
    5. 5xx(서버 오류): 서버가 명백히 유효한 요청 충족 실패


<< 2.5 httpie >>

1) Httpie 설치
    -> pip install --upgrade httpie

2) Httpie 명령어
    * httpie 명령어는 "http" 키워드로 시작*

    예) http [flag] [METHOD] URL [ITEM[ITEM]]

    -Json 형식의 요청:
        http --json POST 대상주소 GET인자==값 POST인자=값
    
    -HTML form 형식의 요청:
        http --form POST 대상주소 GET인자==값 POST인자=값
    (GET, POST인자가 있으면 쓰고 없으면 안 씀.)

