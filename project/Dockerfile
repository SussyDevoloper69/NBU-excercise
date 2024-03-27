# start from base
FROM ubuntu:16.04


RUN apt-get -yqq update && apt-get -yqq upgrade
RUN apt-get -yqq install git maven ant openjdk-8-jdk-headless build-essential python-dev

RUN git clone http://github.com/floodlight/floodlight.git



WORKDIR /floodlight
RUN git submodule init && git submodule update
RUN mvn compile && mvn package
# expose port
EXPOSE 8080
EXPOSE 6653
# start app
CMD [ "java", "-jar", "target/floodlight.jar" ]
