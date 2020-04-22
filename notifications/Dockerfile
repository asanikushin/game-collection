FROM python:3.8-slim
COPY requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /requirements.txt

COPY utils utils

COPY notifications notifications
RUN cp notifications/notifications.py ./ && chmod +x notifications.py

ENTRYPOINT ["./notifications.py"]
