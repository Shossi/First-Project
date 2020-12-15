FROM Centos:8
RUN yum install -y python3 && pip3 install requests && pip3 install argparse
ARG city="israel"
COPY . /api2.py
CMD python3 api2.py -c $city
