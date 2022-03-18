class Demo:
    A = 10
    def __init__(self):
        self.B = 20
        print("Inside Constructor")

    def fun_instance(self):
        print("Inside Instance method")

    @classmethod
    def fun_class(cls):
        print("Inside Class method")

    @staticmethod
    def fun_static():
        print("Inside static method")

    def __del__(self):
        print("Inside Deestructor")

def main():
    Demo.fun_class()
    Demo.fun_static()
    obj = Demo()
    obj.fun_instance()

    # obj.fun_static()
    # obj.fun_class()



if __name__ == "__main__":
    main()
    print("End of Application")

    #instance method
        #no decorator
        #self as a parametor
        #call by the object name
        # can access instance as well as class varaible

    #class method
        #classmethod as a decorator
        #cls as parametor
        #call by class name(by object also allowd)
        # can access only class variable
     #static method
        #static method as decorator
        #no parameter
        #call by class name( by object also allowed)
        # can access only class varaible using class name