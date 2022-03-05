FROM ubuntu

RUN  apt update 

RUN apt install python3 -y

RUN apt install pip -y

RUN pip3 install flask

COPY  . /tmp/

ENTRYPOINT [ "python3" ]
 
CMD [ "tmp/new_flask_app.py"]
