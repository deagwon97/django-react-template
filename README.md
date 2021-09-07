# Django-React-template

## > Cool template for on premise web server.

1. Develop web applications using Django-REST api and React.
2. Implement asynchronous operation in django using Redis and Celery.
3. Implement and automate SSL authentication tasks using the nginxproxy/acme-companion and nginxproxy/nginx-proxy containers.

- Backend Framework
<p align="center"><img src="https://img.shields.io/badge/Dajngo-092E20?style=flat-square&logo=django&logoColor=white"/></a><img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=Celery&logoColor=white"/></a><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=Redis&logoColor=white"/></a></p>

- Frontend Framework (Templete from: https://github.com/devias-io/material-kit-react)
<p align="center">
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=black"/></a>
</p>

- Proxy Server & SSL Certificate Authorities
<p align="center">
<img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=Nginx&logoColor=white"/></a><img src="https://img.shields.io/badge/Let's Encrypt-003A70?style=flat-square&logo=letsencrypt&logoColor=white"/></a>
</p>

- Tool for defining and running multi-container
<p align="center">
<img src="https://img.shields.io/badge/Docker compose-2496ED?style=flat-square&logo=Docker&logoColor=white"/></a>
</p>

## > docker-compose.prod.yml

```yml
version: '3.8'

services:

  backend:
    container_name: backend
    restart: always
    build:
      context: .
      dockerfile: ./backend/Dockerfile
    volumes:
      - ./backend:/workdir/backend
    command: bash -c "cd ./backend && gunicorn --workers=3 --bind 0.0.0.0:8000 --preload backend.wsgi:application"
    expose:
      - 8000
    env_file:
      - ./backend.env.prod

  redis:
    image: redis
    restart: always
    container_name: redis
    expose:
      - 6379
    command: redis-server
    healthcheck:
      test: 'redis-cli -h 127.0.0.1 ping'
      interval: 3s
      timeout: 1s
      retries: 5

  celery:
    container_name: celery
    build:
      context: .
      dockerfile: ./backend/Dockerfile
    volumes:
      - ./backend:/workdir/backend
    command: bash -c "cd ./backend && python -m pip install -r requirements.txt && celery -A backend worker -l info"
    volumes:
      - ./backend:/workdir/backend
    env_file:
      - ./backend.env.prod
    depends_on:
      - backend
      - redis

  frontend:
    container_name: frontend
    image: nginx:latest
    expose:
      - 80
    volumes:
      - ./frontend/build:/workdir/build
      - ./frontend/front-nginx/front.conf:/etc/nginx/conf.d/default.conf
    env_file:
      - ./frontend.env.prod

  nginx-proxy:
    container_name: nginx-proxy
    restart: always
    build: ./nginx
    ports:
      - 80:80
      - 443:443
    volumes:
      - ./backend:/workdir/backend
      - ./nginx/custom.conf:/etc/nginx/conf.d/custom.conf
      - certs:/etc/nginx/certs
      - html:/usr/share/nginx/html
      - vhost:/etc/nginx/vhost.d
      - /var/run/docker.sock:/tmp/docker.sock:ro
    depends_on:
      - backend
      - redis
      - celery
    labels:
      - com.github.jrcs.letsencrypt_nginx_proxy_companion.nginx_proxy

  letsencrypt:
    image: nginxproxy/acme-companion
    container_name: letsencrypt
    depends_on:
      - nginx-proxy
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - certs:/etc/nginx/certs
      - html:/usr/share/nginx/html
      - vhost:/etc/nginx/vhost.d
      - acme:/etc/acme.sh
    env_file:
      - .env.prod.proxy-companion

volumes:
  certs:
  html:
  vhost:
  acme:
```

## Pre Requirements

- ubuntu 20.04
- python 3.8
- npm 6.14.4
- docker 20.10.8
- docker-compose 1.29.2
- open 443 & 80 ports

## 0. make static files

```shell
cd ./fontend
npm install
npm run build
cd ../
```

## 1. production

You need only this line.

```shell
docker-compose -f docker-compose.prod.yml up
```

## 2. development

```shell
# run development docker containers

docker-compose -f docker-compose-dev.yml up

# if you want to find new version of front codes, follow the shell.

cd ./frontend

npm run start

# 환경변수 설정 필요

```

## 3. Without docker (without celery & redis)

- frontend setup

```shell
cd ./frontend

npm install

npm run build
```

- backend setup

```shell
cd ./backend

python -m venv .venv

# linux - activate
. .venv/bin/activate
# window - activate
. .\.venv\Scripts\activate

pip install -r requirement.txt
```

```python

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

```

- run server

```

python manage.py runserver

```

## Reference

- https://docs.djangoproject.com/en/3.2/
- https://ko.reactjs.org/docs/getting-started.html
- http://milooy.github.io/TIL/Django/react-with-django-rest-framework.html#django-rest-framework-%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC
- https://developer0809.tistory.com/92
- https://velog.io/@killi8n/Django-React-%EB%A1%9C-%EC%B2%AB-%ED%99%94%EB%A9%B4-%EB%9D%84%EC%9B%8C%EB%B3%B4%EA%B8%B0-55jm970olw

- https://velog.io/@hyeon4137/React-DRF-API%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-velog-%EB%94%B0%EB%9D%BC-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EA%B8%B0-3%EC%9E%A5
- https://github.com/nginx-proxy/nginx-proxy
- https://hub.docker.com/r/nginxproxy/acme-companion

## License

- Licensed under MIT (https://github.com/deagwon97/django-react-template/blob/main/LICENSE)

## Contact To

- Email: azaz09112@gmail.com
