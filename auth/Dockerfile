FROM python:3.8-alpine as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM python:3.8-alpine
COPY --from=builder /install /usr/local

ENV FLASK_APP runner.py
COPY auth/config.py auth/runner.py auth/run.sh ./

RUN chmod +x run.sh

COPY auth/migrations migrations
COPY utils utils
COPY constants constants
COPY auth auth
ENTRYPOINT ["./run.sh"]
