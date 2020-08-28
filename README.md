# Sign in with Hongik

홍익대학교 학생임을 인증할 수 있는 Python 코드입니다.
[홍익대학교 웹사이트](https://hongik.ac.kr) 로그인 성공 여부를 확인합니다.

## How to use

[Requests](https://github.com/psf/requests) 모듈이 필요합니다.

```Console
pip install requests
```

코드 사용법

```Python
signin_with_hongik('hongik_id', 'hongik_password')
```

클래스넷 로그인 성공 시 True, 실패 시 False를 반환합니다.
