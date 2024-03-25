import threading
import time
start=time.time()

def task1():
    print("Task 1 started")
    for i in range(3):
        print(f"Task 1: {i}")
    print("Task 1 completed")

def task2():
    print("Task 2 started")
 
    for i in range(3):
        print(f"Task 2: {i}")
    print("Task 2 completed")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
end=time.time()

print(f"main thread completed :{end-start}")