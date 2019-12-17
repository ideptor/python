# python

가상환경 설치
```
$python -m venv 가상환경이름
```


가상환경 실행
```
$./가상환경폴더/Script/activate.bat  (윈도우 환경)
```
보안에러 발생시 PowerShell 아이콘 우클릭 → 관리자모드로 실행 후 (관리자 모드로 실행하면 System32에서 시작)
또는 `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` 를 입력해준다.

실행화면
```
(가상환경이름)$pip list
```

가상환경 종료
```
(가상환경이름)$deactivate
(가상환경이름)$./가상환경폴더/Script/deactivate.bat  (윈도우 환경)
```
[출처] [파이썬으로 개발 시작하기 CAMP](https://blog.naver.com/5yshil/221353705316)

tngu
## 패키지 목록 내보내기 & 설치하기

현재 dependency 내보내기
```
(vision)$ pip freeze > requirements.txt
(vision)$ more requirements.txt
astroid==2.3.3
colorama==0.4.3
h5py==2.10.0
```

`requirements.txt`에 있는 dependency 설치하기
```
pip install -r requirements.txt
```






