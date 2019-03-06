# -*- coding: utf-8 -*-
from socket import *
import argparse
import json
import time
import sys
import log.lesson5_server_log_config
from log.lesson5_server_log_config import *
#from __future__ import print_function
import functools
import traceback
import sys

INDENT = 4*' '

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        callstack = '\n'.join([INDENT + line.strip() for line in traceback.format_stack()][:-1])
        mycallstack = traceback.format_stack()
        lenofmycallstack = len(traceback.format_stack())
        lastcall = mycallstack[lenofmycallstack-2].replace('\n', ',')
        #print(lastcall)
        #print(callstack)
        #print(f'TRACE: calling {func.__name__}() '
        #      f'with {args}, {kwargs}')
        called= f'TRACE: calling {func.__name__}() '+f'with {args}, {kwargs}'
        file_logger.info(lastcall)
        file_logger.info(called)
        original_result = func(*args, **kwargs)
        returned = f'TRACE: calling {func.__name__}() '+f'returned {original_result!r}'
        file_logger.info(returned)
        #print(f'TRACE: {func.__name__}() '
        #      f'returned {original_result!r}')

        return original_result
    return wrapper

@trace
def parsing():
    file_logger.info("server parameters parsing")
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="port number", type=int)
    parser.add_argument("-a", help="ip addr", type=str)
    args = parser.parse_args()
    portnumber = args.p
    ipaddress = args.a
    if ipaddress is None:
        ipaddress = ''
    if portnumber is None:
        portnumber = 7779
    nottesting = True
    parameters = [ipaddress, portnumber, nottesting]
    return parameters

@trace
def myserverup(myinparameters):
    file_logger.info("server connection")
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((myinparameters[0], myinparameters[1]))
        s.listen(5)
    except:
        file_logger.error("server socket can't open")
        sys.exit()

    endless = True
    try:
        while endless:
            try:
                client, addr = s.accept()
            except:
                file_logger.error("server socket can't accept connection")
                sys.exit()

            try:
                msgfromclient = client.recv(102400).decode('utf-8')
            except:
                file_logger.error("server socket can't receive data")
                sys.exit()

            msgfromclientinjson = json.loads(msgfromclient)
            #print(msgfromclientinjson)
            print("There is request on connection from %s" % str(addr))
            file_logger.info("received message is "+str(msgfromclientinjson))
            myresponse = {}
            myresponse["response"] = 100
            myresponse["time"] = time.time()
            myresponseintext = json.dumps(myresponse)
            print(myresponseintext)
            try:
                client.send(myresponseintext.encode('utf-8'))
            except:
                file_logger.error("server socket can't send data")
                sys.exit()

            client.close()
            if myinparameters[2] == False:
                endless = False
                return myresponseintext
    finally:
        s.close()


if __name__ == '__main__':
    log.lesson5_server_log_config.setupServerLog()
    file_logger = log.lesson5_server_log_config.logging.getLogger("main")
    #mysetup = log.lesson5_server_log_config.mysetup
    #file_logger.addHandler(mysetup)
    print(type(file_logger))
    myparameters = parsing()
    myserverup(myparameters)
