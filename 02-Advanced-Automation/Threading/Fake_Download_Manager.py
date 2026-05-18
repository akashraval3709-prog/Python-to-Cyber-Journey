import threading
import time

files = [
    'movie.mkv',
    'python.pdf',
    'linux.iso'
]

thread_list=[]
def downloader(file):
    for i in range(1,6):
        time.sleep(1.5)
        print(f'{threading.current_thread().name} | {file} -> {20*i}%')
        time.sleep(1)
    print(f'{file} Download Complete')

        
        

for index,file in enumerate(files):
    t=threading.Thread(target=downloader,args=(file,),name=f'Thread{index+1}')
    thread_list.append(t)
    t.start()
    
for thread in thread_list:
    thread.join()
