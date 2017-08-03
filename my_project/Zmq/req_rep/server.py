# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://192.168.252.1:5555")
while 1:
    message = socket.recv()
    print message
    time.sleep(1)
    socket.send("server response!")


