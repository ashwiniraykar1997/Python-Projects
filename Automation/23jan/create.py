def main():
    print("Enter file name that you want to create:")
    name = input()

    fd = open(name,'x')
    print("File gets created with information as:",fd)
if __name__ =="__main__":
    main()