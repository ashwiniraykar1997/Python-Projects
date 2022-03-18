#Arbitary argument in function
def fun(*value):
    print(value)
    print(type(value))

def main():
    fun(10,20,30,40,50)

if __name__ == "__main__":
    main()