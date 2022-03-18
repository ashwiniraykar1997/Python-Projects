
def fun(i=0):
    if (i < 5):
        print(i)
        i = i + 1    # i++
        fun(i) #     recursive call


def main():
    fun(0)

if __name__ == "__main__":
    main()