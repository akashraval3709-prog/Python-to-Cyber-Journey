import threading
import time

# Countdown function
def countdown(name, seconds):

    # Reverse countdown
    for i in range(seconds, 0, -1):

        print(f'Timer {name}: {i}')

        time.sleep(1)

    print(f'Timer {name} Finished')


# Thread create
t1 = threading.Thread(
    target=countdown,
    args=('A', 5)
)

t2 = threading.Thread(
    target=countdown,
    args=('B', 3)
)

print('All Timers Started')

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print('All Timers Completed')
