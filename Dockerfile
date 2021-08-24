FROM ubuntu:latest
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt install -y python3 \
    && apt install time
RUN date
WORKDIR /opt
COPY cpu-usage.py .
CMD time python3 cpu-usage.py