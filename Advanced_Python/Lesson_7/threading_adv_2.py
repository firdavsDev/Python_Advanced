############### GIL, threading, multiprocessing, Lock ###############

# GIL - Global Interpreter Lock
# GIL is a mutex (mutual exclusion lock) that prevents multiple native threads from executing Python bytecodes at once.
# This lock is necessary mainly because CPython's memory management is not thread-safe.
# (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)
# With GIL, only one thread can hold the control of the Python interpreter.
# This means that only one thread can be in a state of execution at any point in time.
# This simplifies the CPython's memory management.


# threading
# The threading module offers both local and global thread management facilities.
# The local facilities are intended for use by thread-aware modules that need to manage their own state on a per-thread basis.
# The global facilities are intended for use by higher-level threading users, such as network servers.
# The module also provides a higher level threading API, in the form of the Thread class.
# This class is a subclass of the class defined in the _thread module, and can be used in the same way.
# The module also provides a convenience function, called start_new_thread(), which starts a new thread and returns its identifier.

# multiprocessing
# The multiprocessing module offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads.
# Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
# It runs on both Unix and Windows.

# Lock
# The Lock class implements a simple locking mechanism.
# It is not owned by a particular thread, but rather by the process in which it was created.
# It is created in the unlocked state.
# It has two methods, acquire() and release().
# When the state is unlocked, acquire() changes the state to locked and returns immediately.
# When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns.
# The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately.
# If an attempt is made to release an unlocked lock, a RuntimeError will be raised.


import threading
import multiprocessing
import time
import random
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(d, lock):
    lock.acquire() # lock
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    lock.release() # unlock
    for i in range(5):
        time.sleep(random.random())
        with lock:
            d[i] = i
            logging.debug(d)

def worker2(d, lock):
    lock.acquire()
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    lock.release()
    for i in range(5):
        time.sleep(random.random())
        with lock:
            d[i] = i
            logging.debug(d)

if __name__ == '__main__':
    # thread

    # d = {}
    # lock = threading.Lock()
    # t1 = threading.Thread(target=worker1, args=(d, lock))
    # t2 = threading.Thread(target=worker2, args=(d, lock))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print(d)

    # process

    d = multiprocessing.Manager().dict()
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=worker1, args=(d, lock))
    p2 = multiprocessing.Process(target=worker2, args=(d, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(d)




