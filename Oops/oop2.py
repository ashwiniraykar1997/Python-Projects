class Demo:
    A = 10
    B = 20
    def __init__(self):
        self.C = 30
        self.D = 40


def main():


    print("Value of A:",Demo.A)
    print("Value of B:",Demo.B)
    obj1 = Demo()
    obj2 = Demo()
    print("value of c from obj1:",obj1.C)
    obj1.C = 0
    print("Value of d from obj2:",obj2.C)
    print("value of c from obj1:",obj1.C)

if __name__ == "__main__":
    main()