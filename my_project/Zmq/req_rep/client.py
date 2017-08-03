# !/usr/bin/python
# -*- coding:utf-8 -*-
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.252.1:5555")

while 1:
    data = raw_input("input you data:")
    if data == 'q':
        sys.exit()
    socket.send(data)
    response = socket.recv();
    
    print response


