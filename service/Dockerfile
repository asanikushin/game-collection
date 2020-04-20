FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev grpc linux-headers make g++
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENV FLASK_APP runner.py
COPY service/config.py service/runner.py service/run.sh ./

RUN chmod +x run.sh runner.py

COPY pb pb
COPY service/migrations migrations
COPY utils utils
COPY constants constants
COPY service service
ENTRYPOINT ["./run.sh"]
