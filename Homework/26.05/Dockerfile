FROM python:3.8-alpine
USER root
EXPOSE 5001
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP=convertor.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=5001"]
