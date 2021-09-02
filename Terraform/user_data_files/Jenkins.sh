#!/bin/bash
sudo apt update -y
sudo apt -y install docker.io
sudo systemctl start docker
mkdir /home/ubuntu/jenkins_home
sudo chmod 777 /home/ubuntu/jenkins_home
sudo docker run -d -v /home/ubuntu/jenkins_home:/var/jenkins_home -p 80:8080 -p 50000:50000 jenkins/jenkins:lts
