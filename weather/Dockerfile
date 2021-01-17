FROM python:3.8
USER root
RUN pip3 install -r requirements.txt
EXPOSE 5000
USER root
COPY send.py api2.py config.json /
ENV FLASK_APP=api2.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host 0.0.0.0"]
