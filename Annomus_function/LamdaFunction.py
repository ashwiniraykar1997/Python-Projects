# Lambda function concepts

# Named function
def Add(a,b):
    return a+b

#lamda function
#syntax
# lamda parameter:Expression
Addx = lambda a,b: a+b

def main():
    ret = Add(10,20)
    print("Addition is:",ret)

    ret = Addx(10,20)
    # ret = 10 + 20
    print("Addition is:",ret)
    print(type(Add))
    print(type(Addx))
    print((lambda a,b: a+b))


if __name__ == "__main__":
    main()







[5,4,7,6,8]
[4,6,8]
[6,8,10]
24