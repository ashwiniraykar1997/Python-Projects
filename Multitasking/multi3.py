import os
import multiprocessing

def fun(X):
    print("PID is of fun :",os.getpid())
    print("inside fun")
    for i in range(X):
        print("Fun :",i)

def gun(X):
    print("PID is  of gun :", os.getpid())
    print("inside gun")
    for i in range(X):
        print("Gun :", i)

def main():
    print("PID is of parent process:", os.getpid())
    fun(5)
    gun(10)

if __name__=="__main__":
    main()

#serial programing or single process multitasking
