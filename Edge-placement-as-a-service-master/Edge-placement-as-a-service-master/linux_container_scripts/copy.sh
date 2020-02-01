#!/bin/bash
docker cp $1:/$2 /home/ece792/temp/
sleep 5
docker cp /home/ece792/temp/$2 $3:/home/$2

# $1 source container
# $2 file
# $3 destination container
