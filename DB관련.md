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

- use {db이름}
- show tables;