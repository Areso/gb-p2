from socket import *
import argparse
import sys


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
        msgfromclient = client.recv(1024).decode('utf-8')
        print("Получен запрос на соединение от %s" % str(addr))
        timestr = msgfromclient*3
        timestr = timestr.encode('utf-8')
        client.send(timestr)
        client.close()
finally:
    s.close()
