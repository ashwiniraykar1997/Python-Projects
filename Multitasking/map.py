import time
import multiprocessing
import os

def CheckEvenOdd(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    time.sleep(2)
    print('PID is {} Input : {} results {}'.format(os.getpid(),x, CheckEvenOdd(x)))

if __name__ == '__main__':
    print("Mult processed application with pool : ")

    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0, 5

                                        ))#first paramter(name of your task) ad second parameter(input you want to give that process)
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime - starttime} seconds")


    #this map function is diffrent as filter ,map ,reduce function in python.