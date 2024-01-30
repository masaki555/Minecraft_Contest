FROM ubuntu:latest

ENV HOME /root

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt-get -y update
RUN apt-get -y install -y libopencv-dev wget init systemd
RUN apt-get -y install git
RUN apt-get install -y python3 python3-pip

RUN pip install --upgrade pip
RUN pip install opencv-python

RUN git clone https://github.com/ultralytics/yolov5
RUN pip install -r /yolov5/requirements.txt