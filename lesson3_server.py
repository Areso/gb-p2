# -*- coding: utf-8 -*-
from socket import *
import argparse
import json
import time
import sys
import log.lesson5_server_log_config
from log.lesson5_server_log_config import *


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
