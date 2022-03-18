#single level inheritance example
class Base:
    def __init__(self):
        print("Inside Base constructor")
        self.A = 10

    def fun(self):
        print("Base fun")

##############################################################

class Derived(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()

        print("Inside derived consrtcutor")
        self.B = 20

    def gun(self):
        print("Derived gun")

def main():
    bobj = Base()
    dobj = Derived()
    dobj.gun()
    dobj.fun()
    print(dobj.A)

if __name__ == "__main__":
    main()



# class derived:public Base(c ++)
#class derived extends base(java)
