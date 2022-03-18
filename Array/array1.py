import array as ARR

def main():
    print("Demonstration of array in python")

    data = ARR.array('i',[10,20,30,40])

    print(data)
    print("Length of array",len(data))
    print("type of array",type(data))

    # print(data[0])
    # print(data[1])

    for i in range(len(data)):
        print(data[i],end =" ")

    i = 0
    while(i<len(data)):
        print("\n",data[i])
        i = i + 1

    print("typecode of array is",data.typecode)

if __name__ == "__main__":

    main()