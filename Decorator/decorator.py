def division(A,B):
    Ans = 0.0
    Ans = A/B
    return Ans

def main():
    No1 = 0
    No2 = 0
    No1 = int(input("Enter First Number:"))
    No2 = int(input("Enter Second Number:"))
    ret = division(No1,No2)
    print("Division is :",ret)


if __name__ == "__main__":
    main()