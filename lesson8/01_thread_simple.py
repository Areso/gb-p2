# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#                          Запуск простых потоков

import time
from threading import Thread


def clock(interval):
    ''' Функция, которая может быть запущена в потоке
    '''
    while True:
        print("1 > Текущее время: %s" % time.ctime())
        time.sleep(interval)


class ClockThread(Thread):
    ''' Класс-наследник потока
    '''

    def __init__(self, interval):
        super().__init__()
        self.daemon = False
        self.interval = interval

    def run(self):
        while True:
            print("2 > Текущее время: %s" % time.ctime())
            time.sleep(self.interval)


# t = Thread(target=clock, args=(15,))
# t.start()

t = ClockThread(2)
t.start()
t.join()
