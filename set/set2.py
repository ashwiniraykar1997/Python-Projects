print("Enter Number of elemnts")
size = int( input())
# data = {}
data = set()
for i in range(size):
    print("enter elemnt no:",i +1)
    no = int(input())
    data.add(no)

print("Data form set is:",data)

print("Enter data to search")
value = int(input())

if value in data:
    print("Element is  there:")
else:
    print("there is no such elements:")


