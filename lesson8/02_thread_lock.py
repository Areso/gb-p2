# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#           Синхронизация потоков при помощи блокировок (мьютексов)


import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0

COUNT = 100
shared_resource_lock = threading.Lock()


# ++ Работа с блокировками ++
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


# --- Работа без блокировок ---
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1
        print(shared_resource_with_no_lock)


def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1
        print(shared_resource_with_no_lock)


# Выполните несколько запусков программы,
# чтобы увидеть проблему доступа к общей переменной без блокировки

if __name__ == "__main__":
    # t1 = threading.Thread(target=increment_with_lock)
    # t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    # t1.start()
    # t2.start()
    t3.start()
    t4.start()
    # t1.join()
    # t2.join()
    t3.join()
    t4.join()
    print("Глобальная переменная с доступом через блокировку %s" % shared_resource_with_lock)
    print("Глобальная переменная с доступом без блокировки %s" % shared_resource_with_no_lock)
