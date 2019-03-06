import select
from socket import socket, AF_INET, SOCK_STREAM


class ServerChat:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.mainloop_started = False

    def read_requests(self, r_clients, all_clients):
        """ Чтение запросов из списка клиентов
        """
        responses = []  # Словарь ответов сервера вида {сокет: запрос}

        for sock in r_clients:
            try:
                data = sock.recv(10000000).decode('utf-8')
                responses.append(data)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)

        return responses

    def write_responses(self, requests, w_clients, all_clients):
        """ Эхо-ответ сервера клиентам, от которых были запросы
        """

        for sock in w_clients:
            # if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                for resp in requests:
                    sock.send(resp.encode('utf-8'))
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

    def mainloop_start(self):
        """ Основной цикл обработки запросов клиентов
        """
        clients = []

        self.mainloop_started = True

        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.address, self.port))
        s.listen(5)
        s.settimeout(0.2)  # Таймаут для операций с сокетом
        while self.mainloop_started:
            try:
                conn, addr = s.accept()  # Проверка подключений
            except OSError:
                pass  # timeout вышел
            else:
                print("Получен запрос на соединение от %s" % str(addr))
                clients.append(conn)
            finally:
                # Проверить наличие событий ввода-вывода
                wait = 10
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except Exception as ex:
                    pass  # Ничего не делать, если какой-то клиент отключился

                requests = self.read_requests(r, clients)  # Сохраним запросы клиентов
                if requests:
                    self.write_responses(requests, w, clients)  # Выполним отправку ответов клиентам

    def mainloop_stop(self):
        self.mainloop_started = False


if __name__ == "__main__":
    server = ServerChat('localhost', 10000)

    server.mainloop_start()

