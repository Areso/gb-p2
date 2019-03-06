# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#    Синхронизация многих процессов-потребителей через очередь JoinableQueue


import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()
        # Обработать элемент
        print(item) # <- Здесь может быть некоторая обработка элемента
        # Сообщить о завершении обработки
        input_q.task_done()


def producer(sequence, output_q):
    for item in sequence:
        # Добавить элемент в очередь
        output_q.put(item)


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # Запустить несколько процессов-потребителей
    cons_p1 = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p1.daemon = True
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p2.daemon = True
    cons_p2.start()

    # Воспроизвести элементы.
    # Переменная sequence представляет последовательность элементов, которые
    # будут передаваться потребителю. На практике вместо переменной можно
    # использовать генератор или воспроизводить элементы каким-либо другим
    # способом.
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # Дождаться, пока все элементы не будут обработаны
    q.join()