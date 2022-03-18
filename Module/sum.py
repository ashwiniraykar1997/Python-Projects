
def addition(value1,value2):
    ans = 0
    ans = value1 + value2
    return ans

def main():
    no1 = 0
    no2 = 0
    ret = 0

    print("enter First Number:")
    no1 = int(input())

    print("Enter second value:")
    no2 = int(input())

    ret = addition(no1,no2)

    print("Result is ",ret)

if __name__ == "__main__":
    main()