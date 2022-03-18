
def maximum(value1, value2):
    if ( value1 > value2 ) :

        return value1
    else:
        return value2



def main():

    print("Enter First Number:")
    no1 = int(input())

    print("Enter Second Number:")
    no2 = int(input())

    ret = maximum(no1,no2)

    print("Maximum number is:",ret)


if __name__ == "__main__":
    main()
