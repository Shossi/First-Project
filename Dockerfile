
FROM python:3.8
RUN pip3 install requests
USER root
COPY api2.py .
ENTRYPOINT ["python3","./api2.py"]
