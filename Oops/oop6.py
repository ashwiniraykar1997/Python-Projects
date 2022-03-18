class Demo:
    A = 10
    def __init__(self):
        print("Inside Constructor")
        self.B = 20

    def fun_instance(self):
        print("Inside Instance method")
        print(self.A)
        print(self.B)
        print(Demo.A) # this is a correct way to access class varaible

    @classmethod
    def fun_class(cls):
        print("Inside Class method")
        print(cls.A)
        print(Demo.A)
        # print(cls.B)



    @staticmethod
    def fun_static():
        print("Inside static method")
        print(Demo.A)
        #



    def __del__(self):
        print("Inside Deestructor")

def main():

    Demo.fun_static()



if __name__ == "__main__":
    main()


