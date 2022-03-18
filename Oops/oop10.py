class Base1:
    def __init__(self):
        print("Inside Base1")
        self.A =10
    def fun(self):
        print("Fun of Base1")

class Base2:
    def __init__(self):
        print("Inside Base2")
        self.B = 20

    def gun(self):
        print("gun of Base2")

class Derived(Base1,Base2):
    def __init__(self):
        self.C = 30
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside derived")
    def sun(self):
        print("sun of derived")

def main():
    # bobj1 = Base1()
    dobj = Derived()




if __name__ == "__main__":
    main()


