FROM ubuntu

WORKDIR /app

COPY . .

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy sklearn