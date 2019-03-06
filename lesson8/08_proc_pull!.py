# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#                  Пул процессов для полезных вычислений

import os
import multiprocessing
import hashlib

# Вы можете изменить значения некоторых параметров
BUFSIZE = 8192 # Размер буфера чтения
POOLSIZE = 4   # Количество процессов


def compute_digest(filename):
    ''' Функция, которая будет выполняться в пуле процессов
    '''
    try:
        f = open(filename, "rb")
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(BUFSIZE)
        if not chunk: 
            break
        digest.update(chunk)

    f.close()
    return filename, digest.digest()


def build_digest_map(topdir):
    digest_pool = multiprocessing.Pool(POOLSIZE)
    allfiles = (os.path.join(path, name)
                for path, dirs, files in os.walk(topdir)
                    for name in files)
    digest_map = dict(digest_pool.imap_unordered(compute_digest, allfiles, 20))
    digest_pool.close()
    return digest_map


# Проверка. Измените имя каталога на желаемое.
if __name__ == '__main__':
    digest_map = build_digest_map(".")
    print(len(digest_map))
    print(digest_map)