FROM ubuntu

RUN apt-get update

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip install requests

COPY . tmp/


WORKDIR tmp/

ENTRYPOINT [ "python3" ]

CMD [ "req_resp_httpbin.py" ]

