import sys


def DisplayR(no):
    no = sys.getrecursionlimit()
    print(no)
    # no = no + 1
    DisplayR(no)  #Recursive call

def main():
    DisplayR(0)

if __name__ == "__main__":
    main()