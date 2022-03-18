import marvellous1

def main():
    size = 0
    i = 0
    # no = 0
    data = []
    print(" How many Element you want?")
    size = int(input())

    print("Please enter elemnts:")
    for i in range(size):
        # no = int(input())
        data.append((int(input())))
    print("Your entered data is:",data)

    ret = marvellous1.Addition((data))
    print("Addition is:",ret)




if __name__ == "__main__":
    main()