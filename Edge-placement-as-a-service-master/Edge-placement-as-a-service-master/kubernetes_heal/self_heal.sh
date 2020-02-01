#!/bin/bash

name="$(sudo docker ps -a --filter 'exited=0' --format "{{.ID}}")" && sudo docker start $name
