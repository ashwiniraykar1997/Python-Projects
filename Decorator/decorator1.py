def division(a,b): #0x100

    ans = 0.0
    ans = a / b
    return ans

def SmartDivision(Func_name): #fun_name->0x100
    def inner(a,b): #0x200
        if a < b:
            a,b = b,a
        return Func_name(a,b)  #return 0x100(_,_)
    return inner # return 0x200


division = SmartDivision(division) #division = SmartDivision(0x100)

def main():
    no1 = 0
    no2 = 0
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))
    ret = division(no1,no2) #0x200(5,10)
    print("Division is :",ret)

if __name__ == "__main__":
    main()
