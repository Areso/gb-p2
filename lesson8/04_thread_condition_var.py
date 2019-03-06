# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#               Синхронизация потоков при помощи переменной состояния

from threading import Thread, Condition
import time

items = []
condition = Condition()

class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("Потребитель : нечего получать")

        items.pop()
        print("Потребитель: получен 1 элемент")
        print("Потребитель: доступно {} элементов".format(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(10)
            self.consume()


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Производитель: произведено {} элементов".format(len(items)))
            print("Производитель: остановка производства!!")

        items.append(1)
        print("Производитель: всего произведено {} элементов".format(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(5)
            self.produce()


if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    