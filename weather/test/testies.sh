##!/usr/bin/env bash
#b=$(git branch -r | cut -d '/' -f2 | grep 0. | head -1 )
#a=$(git log | head -1 | awk '{print $2}' | cut -c1-6 )
#echo "$c"
##container="joeyhd/weatherapi:$a-$b" | tr -d '\r'
##sudo docker build -t joeyhd/weatherapi:"$a"-"$b" .
##echo $container
##
##check_result () {
##  RESULT=$?
##    if [ $RESULT == 0 ]; then
##        echo [SUCCESS]
##    else
##        echo [FAIL]
##        exit 1
##    fi
##}
##
##curl http://localhost:80
##check_result
##
#exit 0
