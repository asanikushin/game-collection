FROM python:3.8-alpine as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM python:3.8-alpine
COPY --from=builder /install /usr/local

COPY utils utils
COPY constants constants
COPY notifications notifications
COPY notifications/notifications.py ./
RUN chmod +x notifications.py

ENTRYPOINT ["./notifications.py"]
