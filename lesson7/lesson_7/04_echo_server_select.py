# -------- Эхо-сервер, обрабатывающий "одновременно" несколько клиентов -------
#              Обработка клиентов осуществляется функцией select

import select
from socket import socket, AF_INET, SOCK_STREAM


def read_requests(r_clients, all_clients):
    ''' Чтение запросов из списка клиентов
    '''
    responses = {}      # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('ascii')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses       


def write_responses(requests, w_clients, all_clients):
    ''' Эхо-ответ сервера клиентам, от которых были запросы
    '''

    for sock in w_clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode('ascii')
                # Эхо-ответ сделаем чуть непохожим на оригинал
                test_len = sock.send(resp.upper())
            except:                 # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def mainloop():
    ''' Основной цикл обработки запросов клиентов
    '''
    address = ('', 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)   # Таймаут для операций с сокетом
    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass                     # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)            
        finally:                     
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass            # Ничего не делать, если какой-то клиент отключился    
    
            requests = read_requests(r, clients)      # Сохраним запросы клиентов
            write_responses(requests, w, clients)     # Выполним отправку ответов клиентам                   


print('Эхо-сервер запущен!')
mainloop()
