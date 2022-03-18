import os
import threading

def fun(X):
    print("PID is of fun :",os.getpid())
    print("PPID of fun :", os.getppid())
    print("Thread name :", threading.current_thread().name)
    print("inside fun")
    for i in range(X):
        print("Fun :",i)

def gun(X):
    print("PID is  of gun :", os.getpid())
    print("PPID of gun :",os.getppid())
    print("Thread name :",threading.current_thread().name)
    print("inside gun")
    for i in range(X):
        print("Gun :", i)

def main():
    No = 5
    print("PID is of parent process:", os.getpid())
    thread1 = threading.Thread(target = fun, args = (No,),name='funThread')
    thread2 = threading.Thread(target = gun, args = (No,),name='gunThread')



    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")

if __name__=="__main__":
    main()

#serial programing
