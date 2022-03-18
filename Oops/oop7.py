class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20#private vraible of classs (this is abstraction)

    def fun(self):
        print("Inside fun")
        print(self.A)
        print(self.__B)


def main():
    obj = Demo()
    print(obj.A)
    obj.fun()
    # print(obj.B)

if __name__ == "__main__":
    main()

    #A is public variable
    #B is private variable