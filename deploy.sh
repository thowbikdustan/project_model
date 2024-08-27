#!/usr/bin/env bash

sudo docker-compose kill
sudo cosign verify --key /home/dustan/cosign.pub thowbikdustan/distroless-flask
if [ $? -ne 0 ]; then exit 1; fi
sudo cosign verify --key /home/dustan/cosign.pub thowbikdustan/distroless-nginx
if [ $? -ne 0 ]; then exit 1; fi
sudo docker-compose up -d
