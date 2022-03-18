import os

def fun():
    print("PID is :",os.getpid())
    print("inside fun")
    for i in range(5):
        print("Fun :",i)

def gun():
    print("PID is :", os.getpid())
    print("inside gun")
    for i in range(5):
        print("Gun :", i)

def main():
    print("PID is :", os.getpid())
    fun()
    gun()

if __name__=="__main__":
    main()

#serial programing
