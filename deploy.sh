#!/usr/bin/env bash

sudo docker-compose kill
cat docker-compose.yml | grep image | cut -d ":" -f 2 > images.txt
IMAGE_LIST_FILE="images.txt"
while IFS= read -r IMAGE_NAME; do
    if [ -n $IMAGE_NAME ]; then
        echo "verifying Image: $IMAGE_NAME"

        cosign verify --key /home/ubuntu/cosign.pub $IMAGE_NAME
        if [ $? -ne 0 ]; then echo "Image Verfication Failed" 
            exit 1; fi
    else
        echo "Warning: Found empty line in image list file. Skipping..."
    fi
done < $IMAGE_LIST_FILE
sudo docker-compose up -d
