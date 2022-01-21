FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y openjdk-8-jre && \
    apt-get install -y graphviz && \
    apt-get install -y git && \
    apt-get install -y python3

# RUN wget -O plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.1.2020.15.jar/download

COPY script.py /script.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "sh", "-c", "/entrypoint.sh" ]