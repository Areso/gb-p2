# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля threading ------------------

#           Сервер и клиент обрабатывающие соединения в потоках


import socket
import time
from threading import Thread
import sys

class SockHandler():
    ''' Базовый класс для работы с сокетом
    '''
    def __init__(self, sock):
        self.sock = sock
        self.is_alive = False

    def __call__(self):
        ''' Класс-наследник должен выставить флаг is_alive = True '''
        raise NotImplemented

    def stop(self):
        self.is_alive = False


class TimeServer(SockHandler):
    ''' Класс для отправки времени через заданные интервалы
    '''
    def __init__(self, sock, timeout):
        super().__init__(sock)
        self.timeout = timeout

    def __call__(self):
        self.is_alive = True
        while True:
            if not self.is_alive:
                break
            time.sleep(self.timeout)
            data = str(time.ctime())
            self.sock.sendall(data.encode('utf-8'))
                

class ConsoleHandler(SockHandler):
    ''' Обработчик ввода из консоли 
    '''
    def __call__(self):
        while True:
            data = input("<< ")
            if data == 'exit':
                break
            self.sock.sendall(data.encode('utf-8'))    


class Receiver(SockHandler):
    ''' Класс-получатель информации из сокета
    '''
    def __call__(self):
        self.is_alive = True
        while True:
            if not self.is_alive:
                break
            data = self.sock.recv(1024).decode('utf-8')
            if data:
                print("\n>> ", data)
            else:
                break    


class Server:
    ''' Класс сервера. 
        Слушает сеть. Периодически отправляет клиенту текущее время.
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start_serve(self):
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_sock.bind((self.ip, self.port))
        self.serv_sock.listen(1)
        print('wainting for client...')
        client, addr = self.serv_sock.accept()

        print('client has come :)')
        listener = Receiver(client)
        th_listen = Thread(target=listener)
        th_listen.daemon = True    

        sender = TimeServer(client, 5)
        th_sender = Thread(target=sender)    
        th_sender.daemon = True

        th_listen.start()
        th_sender.start()

        while True:
            if not th_listen.is_alive:
                break
            if not th_sender.is_alive:
                break

        self.serv_sock.close()


class Client:
    ''' Класс клиента. Подключается к серверу, отправляет данные из консоли
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start_session(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

        listener = Receiver(self.sock)
        th_listen = Thread(target=listener)
        th_listen.daemon = True    

        sender = ConsoleHandler(self.sock)
        th_sender = Thread(target=sender)    
        th_sender.daemon = True

        th_listen.start()
        th_sender.start()

        while True:
            if not th_listen.is_alive:
                break
            if not th_sender.is_alive:
                break

        self.sock.close()


if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'c':
        client = Client('localhost', 7777)  
        client.start_session()      
    elif sys.argv[1] == 's':
        server = Server('localhost', 7777)
        server.start_serve()
    else:
        print('wrong option')    


                