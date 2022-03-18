# import marvellous
# import marvellous as m
from marvellous import *
import infosystem

def main():
    print("inside module:",__name__)
    no1 = int(input("Enter first value:"))
    no2 = int(input("Enter second value:"))

    ret = addition(no1, no2)
    print("Addition is", ret)

    ret = infosystem.substration(no1,no2)
    print("substrction",ret)

if __name__ == "__main__":
    main()