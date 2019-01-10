from socket import *
import argparse
import json
import time


def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="port number", type=int)
    parser.add_argument("-a", help="ip addr", type=str)
    args = parser.parse_args()
    portnumber = args.p
    ipaddress = args.a
    if ipaddress is None:
        ipaddress = 'localhost'
    if portnumber is None:
        portnumber = 7777
    parameters = [ipaddress, portnumber]
    return parameters


def myconnect(myinparameters):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((myinparameters[0], myinparameters[1]))
    msg = {}
    msg["action"] = "presence"
    msg["time"] = time.time()
    msg["type"] = "status"
    user = {}
    user["account_name"] = "Areso"
    user["status"] = "online"
    msg["user"] = user
    msgstr = json.dumps(msg)
    s.send(msgstr.encode('utf-8'))
    data = s.recv(1000000)
    print('Message: ', data.decode('utf-8'), ', with length ', len(data), ' bytes')
    s.close()


if __name__ == '__main__':
    myparameters = parsing()
    myconnect(myparameters)
