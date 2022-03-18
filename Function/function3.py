#default argument
def Area(radius,PI = 3.14):
    ans = 0.0
    ans = PI * radius * radius
    return ans

def main():
    print("Enter radius of circle")
    value = float(input())

    ret = 0.0
    ret = Area(value,7.10)
    # ret = Area(PI = 7.10,radius= value)
    print("Area of circle",ret)


if __name__ == "__main__":
    main()