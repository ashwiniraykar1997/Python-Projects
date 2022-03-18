#List
#Sequential
#Index
#Data is mutable
#List is mutable
#Allows Duplicate
#Hetrogenoius

Data= [11,21,51,101,3.14]
print(type(Data))
print("Length of list is",len(Data))
print("Actual Data is:",Data)

print("Data from 0th index:",Data[0])
print("Data from 3rd index:",Data[3])

Data[0] = 12
print("New data is",Data[0])
print("**",Data)


Data.append(111)
print(Data)

Data.insert(2,51)
print(Data)

print(Data[-1])
print(Data[-2])
print("Data[1:3",Data[1:3])
print("Data[0:4]",Data[0:4])

# Data.insert[-1:50]
# print(Data)