FROM python:3.7.0-alpine3.8
USER root
WORKDIR /homework
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=ftest.py
CMD flask run --host=0.0.0.0