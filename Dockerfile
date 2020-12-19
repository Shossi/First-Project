
FROM python:3.8
RUN pip3 install requests
USER root
COPY send.py api2.py config.json /
ENTRYPOINT ["python3","./api2.py"]
