FROM python:alpine

ENV APP /usr/src/web
WORKDIR $APP

RUN apk add --update --no-cache \
    build-base \
    linux-headers \
    pcre-dev

COPY requirements.txt $APP
RUN pip install -r requirements.txt

COPY . $APP

CMD ["uwsgi", "uwsgi.ini"]
