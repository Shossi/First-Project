FROM python:3.8-alpine
USER root
EXPOSE 5000
COPY * /
RUN pip3 install -r requirements.txt
ENV FLASK_APP=api2.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
