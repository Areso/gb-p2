# ------- Программа клиента, бесконечно запрашивающего текущее время ---------

from socket import *
from random import randint
    
s = socket(AF_INET, SOCK_STREAM)    # Создать сокет TCP
s.connect(('localhost', 8888))      # Соединиться с сервером

while True:
    tm = s.recv(1024)               # Принять не более 1024 байтов данных
    print("Текущее время: %s" % tm.decode('ascii'))

