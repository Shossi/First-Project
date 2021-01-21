FROM python:3.8
USER root
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY send.py api2.py config.json requirements.txt /
ENV FLASK_APP=api2.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host 0.0.0.0"]
