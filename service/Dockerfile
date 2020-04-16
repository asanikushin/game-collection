FROM python:3.8.2-alpine

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

ENV FLASK_APP runner.py
COPY service/config.py service/runner.py service/run.sh ./

RUN chmod +x run.sh runner.py

COPY service/migrations migrations
COPY utils utils
COPY constants constants
COPY service service
ENTRYPOINT ["./run.sh"]
