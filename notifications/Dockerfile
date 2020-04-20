FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev grpc linux-headers make g++
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY pb pb
COPY utils utils
COPY constants constants
COPY notifications notifications
COPY notifications/notifications.py ./
RUN chmod +x notifications.py

ENTRYPOINT ["./notifications.py"]
