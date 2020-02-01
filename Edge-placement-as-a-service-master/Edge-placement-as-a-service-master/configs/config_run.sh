#!/bin/bash
sleep 5
sudo docker cp /home/ece792/$2 $3:$2

sudo docker exec $1 ./$2

# $1 dest docekr
# $2 file




