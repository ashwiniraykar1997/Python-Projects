def outer():#0X100
    print("Inside Outer function")

    def inner():#0X200
        print("Inside Inner function")

    return inner#return function object(0x200)

    # return inner()#return function value.this is call to the inner function

def main():
    func_name = outer()# this is call to the outer function
    func_name()# this is used to call the  inner function
    #inner() func_name is internally inner function.insdie func_name contain hashcode of that inner() function

if __name__ == "__main__":
    main()




    # one function can call inside another function
    # inside one function can return another function
    # one fucntion can define inside another function
    #name of function is consider as hashcode of that function in python (inner)
    # () in front of any fucntion  this will be fucntion call