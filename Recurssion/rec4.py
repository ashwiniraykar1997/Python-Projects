
def fun():
    #static int i = 0 in c/c++
    i = 0   #local varaible(Auto storage class)
    if (i < 5):
        print(i)
        i = i + 1    # i++
        fun() # recursive call


def main():
    fun()

if __name__ == "__main__":
    main()