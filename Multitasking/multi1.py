import os # if you want to do the system programming in python use import os

def main():
    print("inside main")
    print("PID of current process :",os.getpid())
    print("PID of parent process :",os.getppid())

if __name__=="__main__":
    main()