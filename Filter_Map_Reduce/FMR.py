from functools import reduce
def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def Increment(no):
    return no + 2

def Addition(a,b):
    return a + b


def main():
    data = [5,7,6,8,4]
    print("orignal data",data)

    # filter(function,list)
    newdata = list(filter(CheckEven,data))

    print("Data after filter",newdata)

    # map(function,list)
    incrementdata = list(map(Increment,newdata))

    print("Data after map:",incrementdata)

    # reduce(function,list)
    ret = reduce(Addition,incrementdata)
    print("Data after Reduce is",ret)

if __name__ == "__main__":
    main()