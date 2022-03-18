import os
def main():
    print("Enter file name that you want to open:")
    name = input()



    fd = open(name,"rb")
    data = fd.read(5)
    fd.seek(3,1)
    # fd.seek(-5,2) end
    # fd.seek(3,1) current
    # fd.seek(3,0) begining

    data = fd.read()
    print(data)




if __name__ =="__main__":
    main()

#0 begining
#1 current
#2 end
