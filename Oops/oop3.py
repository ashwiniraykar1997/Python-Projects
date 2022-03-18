class Demo:
    A = 10 #Class variable

    def __init__(self):
        self.B = 30 # instance varaible

    def fun(self):#Instance method
        print("Inside instance method fun")

    @classmethod
    def gun(cls): #class method
        print("Inside class method")


def main():
    print("Value of class variable:",Demo.A)

    Demo.gun()
    obj1 = Demo()
    print("Value of instance variable:",obj1.B)
    obj1.fun()


if __name__ == "__main__":
    main()