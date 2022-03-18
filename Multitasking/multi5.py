import os
import threading

def fun(X):
    print("PID is of fun :",os.getpid())
    print("PPID of fun :", os.getppid())
    print("inside fun")
    for i in range(X):
        print("Fun :",i)

def gun(X):
    print("PID is  of gun :", os.getpid())
    print("PPID of gun :",os.getppid())
    print("inside gun")
    for i in range(X):
        print("Gun :", i)

def main():
    No = 5
    print("PID is of main :", os.getpid())
    print("PPID of main :",os.getppid())
    thread1 = threading.Thread(target = fun, args = (No,))
    thread2 = threading.Thread(target = gun, args = (No,))



    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")

if __name__=="__main__":
    main()

#serial programing
