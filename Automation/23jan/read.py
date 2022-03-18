import os
def main():
    print("Enter file name that you want to open:")
    name = input()

    if os.path.exists(name):

        fd = open(name,"r")
        print(type(fd))

        data = fd.read(52)
        print("Data of file is:",data)
        fd.close()

    else:
        print("there is no such file")

if __name__ =="__main__":
    main()