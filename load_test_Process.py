import time

from multiprocessing import Process, Queue

def worker(id, number, q):
    increased_number = 0

    for i in range(number):
        increased_number += 1

    q.put(increased_number)

if __name__ == "__main__":

    start_time = time.time()
    q = Queue()

    pr1 = Process(target=worker)