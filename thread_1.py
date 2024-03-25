import time
import threading
start=time.perf_counter()

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    print("done sleeping")

threads=[]
for i in range(10):
    t=threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for threads in threads:
    threads.join()


finish=time.perf_counter()
print(f'Finished in :{round(finish-start,2)} seconds') 

