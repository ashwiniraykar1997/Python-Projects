# %%programing type%%
# @@@Scripting type@@@
# print("Enter First number:")
# no1 = int(input())
# print("Enter Second number:")
# no2 = int(input())
# ans = no1 + no2
# print("Addition",ans)


# @@@procedural type@@@
# def Addition(val1,val2):
#     ans = val1 + val2
#     return  ans
# def main():
#     print("Enter first number:")
#     no1 = int(input())
#
#     print("Enter Second number:")
#     no2 = int(input())
#
#     ret = Addition(no1,no2)
#     print("Addition is",ret)
#
# if __name__ == "__main__":
#     main()



# @@@functional type@@@@
# Addition = lambda a,b:(a+b)
#
# print("Enter First number:")
# no1 = int(input())
# print("Enter Second number:")
# no2 = int(input())
#
# ret = Addition(no1,no2)
# print("addition",ret)


# Object oriented type(oop)
#Encapsulation -> class = Charcteristics + Behaviour

#class defination
class Arithematic: #constructor
    def __init__(self,a,b):
        print("Inside init(Constructor)")
        self.no1 = a #Chracteristics
        self.no2 = b #Charcteristrics

    def Addition(self):#behaviour
        ans = self.no1 + self.no2
        return ans




def main():
    print("Enter First number:")
    x = int(input())

    print("Enter second number:")
    y = int(input())

    obj = Arithematic(x,y) #object creation
    ret = obj.Addition()

    print("Addition is",ret)

if __name__ == "__main__":
    main()



























