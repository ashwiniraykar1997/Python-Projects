
data = {'A':10,'B':20,"D":30,51:'D'}
print("Data is",data)
print("type is:",type(data))
print("length is:",len(data))

# print(data[0]) we can not access with index in dictionary
print(data['A'])

for keys in data:
    print(keys,data[keys])



