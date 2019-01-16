# -*- coding: utf-8 -*-
from socket import *
import argparse
import json
import time
import log.lesson5_server_log_config


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
        portnumber = 7777
    nottesting = True
    parameters = [ipaddress, portnumber, nottesting]
    return parameters


def myserverup(myinparameters):
    file_logger.info("server connection")
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((myinparameters[0], myinparameters[1]))
    s.listen(5)
    endless = True
    try:
        while endless:
            client, addr = s.accept()
            msgfromclient = client.recv(102400).decode('utf-8')
            msgfromclientinjson = json.loads(msgfromclient)
            print(msgfromclientinjson)
            print("There is request on connection from %s" % str(addr))
            myresponse = {}
            myresponse["response"] = 100
            myresponse["time"] = time.time()
            myresponseintext = json.dumps(myresponse)
            print(myresponseintext)
            client.send(myresponseintext.encode('utf-8'))
            client.close()
            if myinparameters[2] == False:
                endless = False
                return myresponseintext
            #return myresponseintext
    finally:
        s.close()


if __name__ == '__main__':
    log.lesson5_server_log_config.setupClientLog()
    file_logger = log.lesson5_server_log_config.logging.getLogger("main")
    print(type(file_logger))
    myparameters = parsing()
    myserverup(myparameters)
