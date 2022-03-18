
def Addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():
    print("Enter first number:")
    value1 = int(input())
    print("Enter second number:")
    value2 = int(input())
    #keywards arguments
    ret = Addition(no1 = value1,no2 = value2)
    print("Addition is:",ret)

if __name__ == "__main__":
    main()