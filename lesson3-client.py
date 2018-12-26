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
    ipaddress = 'localhost'

if portnumber is None:
    portnumber = 7777

s = socket(AF_INET, SOCK_STREAM)
s.connect((ipaddress, portnumber))
msg = {}
msg["action"] = "presence"
msg["time"] = time.time()
msg["type"] = "status"
user = {}
user["account_name"] = "Areso"
user["status"] = "online"
msg["user"] = user
msg1 = json.dumps(msg)
s.send(msg1.encode('utf-8'))
data = s.recv(1000000)
print('Месадж: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
s.close()