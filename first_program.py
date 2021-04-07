import numpy as np
import threading
import time

semaphore = threading.BoundedSemaphore(1)


def mean_of_array(some_array=None):
    semaphore.acquire()
    print('Calculatin mean')
    time.sleep(5)
    if some_array:
        print(f'Mean equals {round(np.mean(some_array), 3)}')
    else:
        print('Nothing to calculate, lol')
    semaphore.release()


def var_of_array(some_array=None):
    semaphore.acquire()
    print('Calculatin var')
    time.sleep(5)
    if some_array:
        print(f'Var equals {round(np.var(some_array), 3)}')
    else:
        print('Nothing to calculate, lol')
    semaphore.release()
