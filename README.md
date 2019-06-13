# auth_server
Django auth server

[인증 방식에 대한 고민](https://github.com/publicejh/auth_server/wiki/%EC%9D%B8%EC%A6%9D-%EB%B0%A9%EC%8B%9D%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B3%A0%EB%AF%BC)

## 소개
Django와 JWT 토큰을 사용하여 간단한 인증 서버를 구현

## 환경
- Python 3.7
- Django 2.2
- Pipenv
- MySql 8.0

## Getting Started

### Prerequisites
*환경 분리용 json 파일*

프로젝트 폴더 내부에 설정 폴더(.config_secret/)와 json 파일들이 필요하다.

![config-dir](https://github.com/publicejh/auth_server/blob/master/docs/img/config-dir.png)

환경분리 env
> export AUTH_ENV=development

default: production

development -> config/settings/debug.py 수행

production -> config/settings/deploy.py 수행

#### settings_common.json
```
{
  "django": {
    "secret_key": ""
  }
}
```

#### settings_debug.json
```
 {
  "django": {
    "allowed_hosts": [
      "localhost",
      "127.0.0.1"
    ],
    "databases": {
      "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306"
      }
    }
  }
}
```

#### settings_deploy.json
```
 {
  "django": {
    "allowed_hosts": [
    ],
    "databases": {
      "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "3306"
      }
    }
  }
}
```

### Installation
```bash
$ pwd
/Users/username/Project/auth_server

$ pyenv install 3.7
$ pyenv global 3.7
$ pipenv install
$ pipenv shell
$ cd auth_server
$ python3 manage.py runserver
```

## 기능
- 회원가입
- 로그인
- JWT 토큰 인증
- User 정보 조회

## TODO
 - [ ] logout 행위에 대한 토큰 expire
 - [ ] refresh token
 - [ ] user 정보 변경
