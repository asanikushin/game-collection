FROM python:3.8-alpine
COPY requirements.txt /requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install -r /requirements.txt

ENV FLASK_APP runner.py
COPY auth/config.py auth/runner.py auth/run.sh ./

RUN chmod +x run.sh

COPY auth/migrations migrations
COPY utils utils
COPY constants constants
COPY auth auth
ENTRYPOINT ["./run.sh"]
