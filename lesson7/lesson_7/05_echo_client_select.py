#  Программа клиента, отправляющего/читающего простые текстовые сообщения на сервер

from socket import *
from select import select
import sys

ADDRESS = ('localhost', 10000)

def echo_client():
    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет авторматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect(ADDRESS)   # Соединиться с сервером
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'exit':
                break
            sock.send(msg.encode('ascii'))     # Отправить!
            data = sock.recv(1024).decode('ascii')
            print('Ответ:', data)


if __name__ == '__main__':
    echo_client()
