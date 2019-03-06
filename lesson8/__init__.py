import queue

q = queue.Queue(maxsize=0)  # FIFO - first in - first out

q = queue.LifoQueue(maxsize=0)  # LIFO - last in - first out

q = queue.PriorityQueue(maxsize=0)


q.qsize()

is_empty = q.empty()

q.full()

q.put()

# q.put_nowait(item) == q.put(item=item, block=False)

q.get()


q.get_nowait()

q.task_done()

q.join()