#!/bin/bash

echo "enter the file you want the script to run on"
read inputfile
echo "enter the file/ip address for which the statstics sould be displayed"
read fd


#awk '{print $1","$4","$5","$6","$7","$8","$9","$10","$11}' /var/log/nginx/access.log > processedlog.csv

awk -v var="$fd" -F',' '$1 ~ var { count++ } END { print count }' $inputfile

