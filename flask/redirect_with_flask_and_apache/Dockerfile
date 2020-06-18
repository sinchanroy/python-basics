FROM httpd:latest

RUN apt-get update && apt-get install -y ca-certificates curl python3-dev python3-pip procps build-essential \
 && apt-get clean -y \
 && apt-get  autoremove -y \
 && rm -rf /var/lib/apt/lists/*

COPY ./server.crt  /usr/local/apache2/conf/
COPY ./server.key  /usr/local/apache2/conf/

COPY my-httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf

COPY my-httpd.conf /usr/local/apache2/conf/httpd.conf

RUN pip3 install flask

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD nohup bash -c "python3 /app/app.py" && httpd -DFOREGROUND