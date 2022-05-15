# Cookie
- 주 사용처
    - 사용자 로그인 세션 관리
    - 광고 정보 트래킹
- 쿠키정보는 항상 서버에 전송
    - 네트워크 트래픽 추가 유발
    - 최소한의 정보만 사용(세션 id, 인증 토큰)
    - 서버에전송하지않고, 웹 브라우저 내부에 저장하려면 웹 스토리지(localStorage, sessionStorage) 
- 보안에 민감한 데이터는 절대 저장 금지 

- 세션 쿠키 : 만료일자 생략시 브라우저 종료시까지만 유지
- 영속 쿠키 : 만료일자 입력시 해당 일자까지 유지

_______
## 도메인
 - 명시 : 명시한 문서 기준 도메인 + 서브 도메인 포함 적용
    - domain = example.org 
        - example.org = 접근
        - dev.example.org = 접근
 - 생략 : 현제 문서 기준 도메인만 적용
    - domain = example.org
        - example.org = 접근
        - dev.example.org = 접근 불가

## 경로 (Path)
    path = /home
- 이 경로를 포함한 하위 경로로만 쿠키 접근 가능
- 일반적으로 path = / 지정

    ex)   
    /home/123 = 접근  
    /home/123/abcd = 접근
    /other = 접근 불가

## 보안
- Secure
    - 쿠키는 http,https 를 가리지 않고 전송
    - Secure 을 적용하면 https에서만 전송
- HttpOnly
    - XSS 공격 방지
    - 자바스크립트에서 접근 불가
    - HTTP 전송에만 사용
- SameSite
    - XSRF 공격 방지
    - 요청 도메인과 쿠키에 설정된 도메인이 같은 경우만 전송