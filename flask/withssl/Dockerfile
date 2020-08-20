from centos:latest

USER root

RUN yum install -y openssl wget python3-devel python3-pip libgomp && \
    yum clean all

COPY . /app

COPY cert.pem /etc/pki/ca-trust/source/anchors/certi.crt

RUN update-ca-trust

WORKDIR /app

EXPOSE 5000

RUN pip3 install flask

CMD python3 app.py

