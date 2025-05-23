FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /opt/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY app.py .

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
