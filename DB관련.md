# 아무거나 일단 적어

> MariaDB 설치
- docker run --name {컨테이너이름} -p 3306:3306 -e MYSQL_ROOT_PASSWORD={패스워드} -d mariadb

- DB 접속
  - docker exec -it {컨테이너이름} mysql -u {USER} -p
  - create database {db이름(NAME)}

```  
# settings.py
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moonam',
        'USER': 'root',
        'PASSWORD': 'ssafy',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
- 위에거 하고 migrate

- use {db이름}
- show tables;

- 근데 조회도 그렇고 sqlite가 훨씬 보기도 편하고 한거같은데 왜 다른 DB툴을 쓰냐??=> sqlite는 사용자가 많아지면 힘들어한다고함