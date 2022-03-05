FROM ubuntu

RUN apt-get update

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip install flask

COPY . tmp/

WORKDIR tmp/

ENTRYPOINT [ "python3" ]

CMD [ "flask_req_resp_demo.py" ]
