# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#                 Синхронизация потоков при помощи событий

import time
from threading import Thread, Event
import random

items = []
event = Event()

class Consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event
    
    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print ('Потребитель: значение %d удалил из списка %s' % (item, self.name))


class Producer(Thread):
    def __init__(self, integers, event):
        Thread.__init__(self)
        self.items = items
        self.event = event
    
    def run(self):
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print ('Производитель: значение %d добавил в список %s' % (item, self.name))
            print ('Производитель: событие установил %s' % self.name)
            self.event.set()
            print ('Производитель: событие удалил %s \n' % self.name)
            self.event.clear()


if __name__ == '__main__':
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
