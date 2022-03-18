def outer():
    print("Inside Outer function")

    def inner():
        print("Inside Inner function")
    inner()

def main():
    outer()

if __name__ == "__main__":
    main()