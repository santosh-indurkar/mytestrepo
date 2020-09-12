FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3-pip
WORKDIR /mytestrepo
COPY . .
RUN pip3 install -r requirements.txt 
CMD ["pytest", "-sv"]
