FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y upgrade
#RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
RUN pip3 install pytest
WORKDIR /mytestrepo/tests
COPY . .
CMD ["pytest", "-sv"]
