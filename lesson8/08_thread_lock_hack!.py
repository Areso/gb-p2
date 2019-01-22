# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля threading ----------------------

#                    Особенность мьютексов в Python

# В Python мьютекс реализован как двоичный семафор, 
# т.е. он не хранит информацию о потоке, который его захватил.

# Поэтому может иметь место ситуация, когда один поток захватывает мьютекс, 
# а другой поток этот же мьютекс тут же освобождает...

from threading import Thread, Lock
import time

done = Lock()

def idle_release():
    print("Running release!")
    time.sleep(5)
    done.release()


done.acquire()

t = Thread(target=idle_release)
t.start()

done.acquire()
print("Странное поведение мьютексов в Python...")    
