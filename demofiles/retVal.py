import threading
import os
import queue

def task1(num, queue): 
    print("\n Current thread: {}".format(threading.current_thread().name)) 
    count = 0
    sum1 = 0
    while count <= 10:
        sum1 = sum1 + num
        num = num + 1
        count = count + 1
    print('\n'+str(sum1))
    queue.put(sum1)


if __name__ == "__main__":

    queue = queue.Queue()

    # print ID of current process 
    print("\n Process ID is: {}".format(os.getpid())) 

    # print name of main thread 
    print("\n Main thread is: {}".format(threading.main_thread().name)) 

    # creating threads 
    t1 = threading.Thread(target=task1, name='t1',args=[10,queue]) 
    t2 = threading.Thread(target=task1, name='t2',args=[21,queue])

    #Store thread names in a list
    pool = [t1,t2]

    #Used to store temporary values
    thread_results = []

    # starting threads
    #Start all threads in thread pool
    for thread in pool:
        thread.start()
        response = queue.get()
        thread_results.append(response)

    #Kill all threads
    for thread in pool:
        thread.join()

    print(thread_results)