import threading
import time

# Shared List
num_list = []

# Lock object
lock = threading.Lock()

def list_append(num):

    print(f'{threading.current_thread().name} waiting for lock...')

    # Critical Section Start
    with lock:

        print(f'{threading.current_thread().name} acquired lock')

        time.sleep(1.5)

        num_list.append(num)

        print(f'Updated List : {num_list}')

        print(f'{threading.current_thread().name} released lock')

    # Critical Section End


# Threads
t2 = threading.Thread(target=list_append, name='Thread-2', args=(50,))
t1 = threading.Thread(target=list_append, name='Thread-1', args=(38,))
t3 = threading.Thread(target=list_append, name='Thread-3', args=(1,))
t4 = threading.Thread(target=list_append, name='Thread-4', args=(2,))

# Start Threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for Completion
t1.join()
t2.join()
t3.join()
t4.join()

print('\nFinal List :', num_list)
