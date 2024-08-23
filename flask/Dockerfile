# Use an official Python image as a parent image
FROM python:3.12-slim as flask_image

RUN apt-get update && apt-get -y upgrade && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev iputils-ping && \
    pip install --upgrade pip
RUN pip install flask && pip install uwsgi

# Using chainguard's python distroless image for final build
FROM cgr.dev/chainguard/python:latest

ENV LD_RUN_PATH=/usr/local/lib
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Copying nessasary components from Layer 1 
COPY --from=flask_image /lib/x86_64-linux-gnu/libcap.so.2 /lib/libcap.so.2
COPY --from=flask_image /lib/x86_64-linux-gnu/libidn2.so.0 /lib/libidn2.so.0
COPY --from=flask_image /lib/x86_64-linux-gnu/libunistring.so.2 lib/libunistring.so.2 

COPY --from=flask_image /usr/local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages
COPY --from=flask_image /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=flask_image /usr/bin/ping /usr/local/bin/ping

# Copying the backend flask application to distroless image
WORKDIR /app
COPY . /app

# Creating an entrypoint to run the application
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
