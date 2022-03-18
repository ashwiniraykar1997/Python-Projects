
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

    obj1 = Arithematic(10,11) #object creation
    ret = obj1.Addition()
    print("Addition is",ret)

    obj2 = Arithematic(20,21)
    ret = obj2.Addition()







    print("Addition is", ret)

if __name__ == "__main__":
    main()



























