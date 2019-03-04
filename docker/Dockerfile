FROM python:3.7-alpine
LABEL mantainer "Tomas Vukasovic <tomowl@pm.me>"

ADD . /coc
WORKDIR /coc

RUN apk update
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip3 install -r docker/requirements.txt
