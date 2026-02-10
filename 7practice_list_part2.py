'''
topics
1.features of list
2.ist is data type or data structure?
3.append list into another list
4.adding two lists
5.accessing list using :
6.length method?
7.insert method?
8.pop method?
9.remove method?
10.delete method?
11.change the list value?
12.split method?
'''
'''
features of list:
1.it can have duplicate values
2.it is mutable in nature(change)
3.it can store multiple data type
4.it is a data type and data structure
'''
from loguru import logger

var_labour_name = ["suma","manish", "labour1", "labour2",100,200,300,400]
var_new_labour = ["rama","mama"]
# instead of extend we can add
#adding two lists
var_labour_name = var_labour_name + var_new_labour
print(f"added {var_labour_name}")

#accessing list using :

print(var_labour_name[1:])

print(var_labour_name[2:5])

#reverse a list
print(var_labour_name[::-1])

#insert to add value at particular index
var_labour_name.insert(4,"manju")
print(var_labour_name)

#length method used to find length of list
print(len(var_labour_name))

#pop method
#used in stack and queue
#delete last element from list
print(var_labour_name.pop())
print(var_labour_name)

# pop a value using index
print(var_labour_name.pop(2))

#remove method
#remove a value by giving the value instead of index
var_labour_name.remove("suma")
print(var_labour_name)

#delete the list
del var_new_labour

#change a list value
var_name = ["maheh","suma","rameh","sumeh"]
print(var_name)
var_name[0]="mahesh"
print(var_name)
#change multiple values
var_name[0:4] = ["mahesh","Suman","ramesh","sumesh"]
print(var_name)

#split method
var_api_endpoint = "https://portal.azure.com/VMINSTANCE/TEST-VM/sub_id/abcd-123/getCredential"

print(var_api_endpoint.split("/"))
var_new_api_list = var_api_endpoint.split("/")
print(var_new_api_list[-2])


