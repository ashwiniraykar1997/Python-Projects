#0x100
def fun():
    print("Inside fun")

#0x200
def gun(func_name):
    print("Inside gun")
    func_name #fun()

def main():
    gun(fun) #gun(0x100)

if __name__ == "__main__":
    main()