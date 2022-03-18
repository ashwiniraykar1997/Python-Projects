import os
def main():
    print("Enter file name that you want to delete:")
    name = input()

    if os.path.exists(name):
        os.remove(name)
        print("File is deleted")

    else:
        print("there is no such file")

if __name__ =="__main__":
    main()