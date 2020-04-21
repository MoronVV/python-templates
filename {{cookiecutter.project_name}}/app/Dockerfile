FROM python:alpine

ENV APP /usr/src/app
WORKDIR $APP

RUN apk add --update-cache \
    gcc \
    musl-dev

COPY requirements.txt $APP
RUN pip install -r requirements.txt

COPY . $APP

CMD ["python", "-u", "main.py"]
