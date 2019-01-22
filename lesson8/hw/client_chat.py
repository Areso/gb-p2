from socket import *
from select import select
import sys
import datetime
import json


class ClientChat:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.name = ''
        self.readMode = False

    def start_chat_loop(self):
        self.name = input('Введите ваше имя в чате: ')
        if "r" == input('Если режим чтения введите r: '):
            self.readMode = True
        # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
        # При выходе из оператора with сокет будет автоматически закрыт
        with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
            try:
                sock.connect((self.address, self.port))  # Соединиться с сервером
            except ConnectionRefusedError as e:
                print("Connection exception")
                return
            while True:
                if self.readMode:
                    dataJsonStr = sock.recv(10000000)
                    data = json.loads(dataJsonStr)
                    print("{} - {} : {}".format(data['time'], data['name'], data['message']))
                else:
                    msgStr = input('Ваше сообщение: ')

                    msg = {
                        "time": datetime.datetime.now().strftime("%H:%M:%S"),
                        "name": self.name,
                        "message": msgStr
                    }

                    if msgStr == 'exit':
                        break
                    sock.send(json.dumps(msg).encode('utf-8'))  # Отправить!


if __name__ == '__main__':
    client = ClientChat('localhost', 10000)

    client.start_chat_loop()