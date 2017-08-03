# !/usr/bin/python
# -*- coding:utf-8 -*-

import zmq

context = zmq.Context()
recive = context.socket(zmq.PULL)
recive.connect('tcp://127.0.0.1:5557')
sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5558')

while 1:
    data = recive.recv()
    print data
    sender.send(data)



