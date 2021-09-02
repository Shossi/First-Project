#!/bin/bash
TAG=$1

check_result () {
  RESULT=$?
    if [ $RESULT==0 ]; then
        echo [SUCCESS]
    else
        echo [FAIL]
        exit 1
    fi
}

containerName=$(echo $TAG | cut -d '-' -f2)
sudo docker rm -f $(sudo docker ps -aq)
sudo docker run -d -p 80:8080 --name "$containerName" "$TAG"
sleep 5
curl http://localhost:80
check_result

exit 0
