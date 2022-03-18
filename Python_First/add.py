def add (x,y):
	
	ans = x + y
	return ans


def main():
	print("hi in main")
	a = int(input("Enter first value:"))
	b = int(input("Enter second value:"))
	ret = add(a,b);
	print("Addition is",ret)
	


if __name__ == "__main__":
	main();