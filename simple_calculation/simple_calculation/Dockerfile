FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip setuptools

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 6543

ENTRYPOINT [ "python3" ]

CMD ["app.py"]