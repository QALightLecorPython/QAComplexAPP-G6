FROM jenkins/jenkins:lts-jdk11
# if we want to install via apt
USER root
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install python3.9 && \
    apt-get -y install python3-pip
# drop back to the regular jenkins user - good practice
USER jenkins