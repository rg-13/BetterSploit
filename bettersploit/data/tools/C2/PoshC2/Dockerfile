# From the Kali Linux base image
FROM kalilinux/kali-rolling

ENV TERM="xterm"
# Update and apt install programs
RUN apt-get update && apt-get full-upgrade -y && apt-get autoremove -y && apt-get install -y git

# Install PoshC2 
ADD . /opt/PoshC2
RUN /opt/PoshC2/Install.sh 

# Working directory
WORKDIR /opt/PoshC2