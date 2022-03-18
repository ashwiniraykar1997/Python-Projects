print("Enter Number of elemnts")
size = int( input())

data = {0}
for i in range(size):
    print("enter elemnt no:",i +1)
    no = int(input())
    data.add(no)

print("Data form set is:",data)

print("Enter data to search")
value = int(input())

if value in data:
    print("Elemnt is  there:")
else:
    print("there is no such elemnt:s")


