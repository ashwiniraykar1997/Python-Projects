import time
import os

def CheckEvenOdd(x):
    print("PID is :", os.getpid())
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def main():
    print("Single process single thread application")
    print("PID is :", os.getpid())
    starttime = time.time()

    for i in range(0, 10):
        time.sleep(2)
        print('Input : {} results {}'.format(i, CheckEvenOdd(i)))

    print('Application took {} seconds'.format(time.time() - starttime))

if __name__ == "__main__":
    main()