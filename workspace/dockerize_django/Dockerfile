FROM ubuntu

RUN apt-get update

RUN apt install python3 -y

RUN apt install pip -y

RUN pip3 install django 

COPY .  tmp/

WORKDIR tmp/

ENV sh="bin/sh"

ENTRYPOINT ["bash"]

# CMD [ "./manage.py" "runserver" ]

CMD [ "script.sh" ]
