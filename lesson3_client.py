from socket import *
import argparse
import json
import time
import sys
import log.lesson5_client_log_config


def parsing():
    file_logger.info("client parameters parsing")
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="port number", type=int)
    parser.add_argument("-a", help="ip addr", type=str)
    args = parser.parse_args()
    portnumber = args.p
    ipaddress = args.a
    if ipaddress is None:
        ipaddress = 'localhost'
    if portnumber is None:
        portnumber = 7779
    parameters = [ipaddress, portnumber]
    return parameters


def myconnect(myinparameters):
    file_logger.info("client connection")
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((myinparameters[0], myinparameters[1]))
    except:
        file_logger.error("server is not answering")
        sys.exit()
    msg = {}
    msg["action"] = "presence"
    msg["time"] = time.time()
    msg["type"] = "status"
    user = {}
    user["account_name"] = "Areso"
    user["status"] = "online"
    msg["user"] = user
    msgstr = json.dumps(msg)
    try:
        s.send(msgstr.encode('utf-8'))
    except:
        file_logger.error("the server can't receive transmitted data")
        sys.exit()

    try:
        data = s.recv(1000000)
    except:
        file_logger.error("the client can't receive transmitted data")
        sys.exit()

    messageforuser = 'Message: '+data.decode('utf-8')+', with length '+str(len(data))+' bytes'
    print(messageforuser)
    s.close()
    return messageforuser


if __name__ == '__main__':
    log.lesson5_client_log_config.setupClientLog()
    file_logger = log.lesson5_client_log_config.logging.getLogger("main")
    print(type(file_logger))
    myparameters = parsing()
    myconnect(myparameters)
