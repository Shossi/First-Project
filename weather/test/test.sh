#!/bin/bash


check_result () {
    if [ $?==0 ]; then
        echo [SUCCESS]
    else
        echo [FAIL]
        exit 1
    fi
}
for city in israel london;do
	sudo docker run weatherapi -c $city
	check_result $city
done
exit 0
