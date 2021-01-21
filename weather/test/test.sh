#!/bin/bash
TAG=$1

check_result () {
  RESULT=$?
  MESSAGE=$1
    if [ $RESULT==0 ]; then
        echo [SUCCESS]
    else
        echo [FAIL]
        exit 1
    fi
}

containerName=$(echo $TAG | cut -d '-' -f2)
sudo docker rm -f $(sudo docker ps -aq)
sudo docker run -d -p 5000:5000 --name "$containerName" "$TAG"
sleep 5
for country in israel; do
  curl -X POST --header "Content-Type: application/json" -d "{\"country\":\"$country\"}" http://localhost:5000
  check_result $country
done

exit 0
