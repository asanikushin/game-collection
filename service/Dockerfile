FROM python:3.8-alpine
COPY requirements.txt /requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev grpc linux-headers make g++ && pip install -r /requirements.txt

ENV FLASK_APP runner.py
COPY service/config.py service/runner.py service/run.sh ./

RUN chmod +x run.sh

COPY pb pb
COPY service/migrations migrations
COPY utils utils
COPY constants constants
COPY service service
ENTRYPOINT ["./run.sh"]
