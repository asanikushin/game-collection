FROM python:3.8-alpine as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM python:3.8-alpine
COPY --from=builder /install /usr/local

ENV FLASK_APP runner.py
COPY service/config.py service/runner.py service/run.sh ./

RUN chmod +x run.sh runner.py

COPY service/migrations migrations
COPY utils utils
COPY constants constants
COPY service service
ENTRYPOINT ["./run.sh"]
