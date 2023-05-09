#!/bin/bash

ssh root@209.38.237.156 'rm -r ~/bookstore'
ssh root@209.38.237.156 'git clone https://github.com/Rainbowdm/bookstore.git'

ssh root@209.38.237.156 'docker stop bookstore-api'
ssh root@209.38.237.156 'docker container rm bookstore-api'

ssh root@209.38.237.156 'docker build -t bookstore-api-build ~/bookstore'
ssh root@209.38.237.156 'docker run --name=bookstore-api -d -e MODULE_NAME="main" -e PORT="8000" -e PRODUCTION="true" -p 8000:8000 bookstore-api-build'

ssh root@209.38.237.156 'docker stop api-nginx'
ssh root@209.38.237.156 'docker rm api-nginx'

#ssh root@209.38.237.156 'docker build -t bookstore-nginx ~/bookstore/nginx-reverse-proxy'
#ssh root@209.38.237.156 'docker run --name=api-nginx -d -p 80:80 bookstore-nginx'

ssh root@209.38.237.156 'docker build -t bookstore-nginx ~/bookstore/nginx-https'
ssh root@209.38.237.156 'docker run --name=api-nginx -d -p 80:80 -p 443:443 -e DOMAIN=bookstores.world -e EMAIL=dim8035@gmail.com bookstore-nginx'