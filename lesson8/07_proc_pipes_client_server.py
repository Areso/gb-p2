# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#   Использование неименованных каналов для клиент-серверного взаимодействия

import multiprocessing


def adder(pipe):
    ''' Серверный процесс
    '''
    server_p, client_p = pipe
    client_p.close()
    while True:
        try:
            x, y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)
    # Завершение
    print("Сервер завершил работу")


if __name__ == '__main__':
    server_p, client_p = multiprocessing.Pipe()
    # Запустить серверный процесс
    adder_p = multiprocessing.Process(target=adder, args=((server_p, client_p), ))
    adder_p.start()

    # Закрыть серверный канал в клиенте
    server_p.close()

    # Послать серверу несколько запросов
    client_p.send((3, 4))
    print(client_p.recv())
    client_p.send(("Hello", "World"))
    print(client_p.recv())

    # Конец. Закрыть канал
    client_p.close()

    # Дождаться, пока завершится серверный процесс
    adder_p.join()
    