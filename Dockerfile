FROM ubuntu:latest

USER root

WORKDIR /minesweeper

COPY . /minesweeper

RUN set -xe && \
    apt update -y && \
    apt install -y python3 python3-pip python3-dev build-essential && \
    pip3 install -r requirements-docker.txt --break-system-packages

EXPOSE 8080

CMD ["python3", "app/app.py"]
