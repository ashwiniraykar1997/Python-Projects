data = {10,20,30,40}
mylist= {10,20,30,40}
print("Mylist is :",mylist)
print("Datatypes is",type(data))

print("length is",len(data))
print("data from set",data)

print("Data travel using loop")
for no in data:
    print(no,end = " ")

data1 = (10,20,30,40,10,10) # duplicate elemnts are allowed but  only once
print("New set data",data1)

data2 =(10,20,30.5,"hello",True)
print("New set data",data2)