import threading

counter = 0
lock = threading.Lock()
def increase():

    global counter

    for i in range(100000):
      with lock:
         counter += 1


t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
