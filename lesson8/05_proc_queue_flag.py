# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#      Синхронизация процессов через очередь Queue и None-флаг в очереди


import multiprocessing


def consumer(input_q):
    while True:
        item = input_q.get()
        if item is None:
            break
        # Обработать элемент
        print(item)  # <- Здесь может быть полезная обработка элемента

    # Завершение
    print("Потребитель завершил работу")


def producer(sequence, output_q):
    for item in sequence:
        # Добавить элемент в очередь
        output_q.put(item)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    # Запустить процесс-потребитель
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    # Воспроизвести элементы.
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # Сообщить о завершении, поместив в очередь сигнальную метку
    q.put(None)

    # Дождаться, пока завершится процесс-потребитель
    cons_p.join()
