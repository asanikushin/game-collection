FROM python:3.8-alpine
COPY requirements.txt /requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev &&  pip install -r /requirements.txt

COPY utils utils
COPY constants constants
COPY notifications notifications
COPY notifications/notifications.py ./
RUN chmod +x notifications.py

ENTRYPOINT ["./notifications.py"]
