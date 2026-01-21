#run multiple parts of a task concurrently with in a single process
#shared memory. share the same memory space
#lightweight
import threading
def task():
    print("thread is running")
t=threading.Thread(target=task)
t.start()
t.join()
print("main thread is done")