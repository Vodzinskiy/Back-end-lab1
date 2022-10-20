FROM python:3.10.7-slim

ENV FLASK_APP=main

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY main /opt/main

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT