def iteration(value):

    for i in range(value):
        print(i)
        print("Hello")


def main():
    value = int(input("Enter how many time you want to iterate for loop:"))

    iteration(value)


if __name__ == "__main__":
    main()
