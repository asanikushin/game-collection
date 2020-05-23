FROM python:3.8-slim
COPY requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /requirements.txt

COPY utils utils
ENV FLASK_APP runner.py

COPY loader loader

RUN cp loader/config.py ./ && cp loader/runner.py ./ \
    && cp loader/run.sh ./ && chmod +x run.sh

ENTRYPOINT ["./run.sh"]
