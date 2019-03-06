# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#                Синхронизация потоков при помощи семафоров

import threading
import time
import random


# Необязательный параметр при создании семафора - внутренний счётчик.
# По умолчанию равен 1.
semaphore = threading.Semaphore(0)

def consumer():
    print ("Потребитель ждёт...")
    # Захватить семафор
    semaphore.acquire()
    ##The consumer have access to the shared resource
    print("Потребитель: получено значение %s " % item)

def producer():
    global item
    time.sleep(5)
    # Создать случайное значение
    item = random.randint(0, 1000)
    print("Поставщик: создано значение %s" % item)
    
    # Освободить семафор (при этом внутренний счетчик увеличивается на 1)
    # Когда счётчик семафора становится больше нуля, то ожидающий поток просыпается
    semaphore.release()


if __name__ == '__main__':
    for i in range (5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print ("Завершено.")