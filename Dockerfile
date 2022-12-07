FROM python:3

RUN apt update
RUN apt install -y python3-pip
RUN apt install -y allure
RUN apt install -y docker.io

RUN python3 -m venv venv
