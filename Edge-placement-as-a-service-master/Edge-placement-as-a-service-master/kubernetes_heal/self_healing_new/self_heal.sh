#!/bin/bash

echo "enter the container to self-heal"
read cname
output=$(sudo docker inspect -f {{.State.Status}} $cname)
if [ "$output" == "exited" ]
then
        sudo docker start $cname
fi

