# !/usr/bin/python
# -*- coding:utf-8 -*-

import zmq

context = zmq.Context()

socket = context.socket(zmq.PULL)
socket.bind('tcp://127.0.0.1:5558')

while 1:
    data = socket.recv()
    print data

