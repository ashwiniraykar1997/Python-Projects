def Division(A,B):
    ans =0.0
    try:
        ans = A/B
    except ZeroDivisionError as obj:
        print("Exception Occurred in zero division error block")
        print("Exception statement :",obj)
    finally: # block which is used to deallocate the resources
        print("inside finally")
    return ans


def main():
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))
    ret = Division(no1,no2)
    print("Division  is :",ret)

if __name__ == "__main__":
    main()