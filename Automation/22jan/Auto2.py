        # import statement (if necessary)
from sys import *
def Addition(ino1,ino2):
    ans = ino1 + ino2
    return ans

#Entry point of automation script
def main():
    print("-------------------Python Machine Learning :Automation Script------------------")
    print("Script name:",argv[0])
    print("Number of arguments accepted:",len(argv)-1)
    if (len(argv)>3) or(len(argv)<2):
        print("Invalid number of arguments")
        print("Use -u flag for usage")
        print("Use -h flag for help")
        exit()

    if(len(argv)==2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage:script is used to perform the addition of 2 number")
            exit()

        elif (argv[1]=="-h"or argv[1] == "-H"):
            print("Help:Name_of_Script First_Argument second_argument")
            print("First_Argument:Any numeric value")
            print("Second_Argument:Any numeric value")
            exit()
        else:
            print("There is no such flag")

    if (len(argv) == 3):
        try:
            iret = Addition(int(argv[1]),int(argv[2]))
            print("Addition is",iret)

        except Exception:
            print("Exception while executing the script")
            print("Please check the input or contact the developer")

# starter of the automation script
if __name__ == "__main__":
    main()