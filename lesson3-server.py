from socket import *
import argparse
import json
import time



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

s = socket(AF_INET, SOCK_STREAM)
s.bind((ipaddress, portnumber))
s.listen(5)

try:
    while True:
        client, addr = s.accept()
        msgfromclient = client.recv(102400).decode('utf-8')
        msgfromclientinjson = json.loads(msgfromclient)
        print(msgfromclientinjson)
        print("Получен запрос на соединение от %s" % str(addr))
        myresponse = {}
        myresponse["response"] = 100
        myresponse["time"] = time.time()
        myresponseintext = json.dumps(myresponse)
        print(myresponseintext)
        client.send(myresponseintext.encode('utf-8'))
        client.close()
finally:
    s.close()
