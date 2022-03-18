from sys import *

def main():
    print("Number of command line arguments are:",len(argv))
    print("Name of application is :",argv[0])
    print("command line argument are :")
    ans = int(argv[1]) + int(argv[2])
    print(ans)




if __name__ =="__main__":
    main()