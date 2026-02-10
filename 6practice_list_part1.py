'''
Topics
1.how to create list
2.what is list
3.what is multi dimensional list
4.how to access data from list
5.methods to access data from list
6. negative indexing
'''
# list - collection of same or different datatype

var_listname = ["suma",100,True,10.5]

#positive index [0,1,2,3]
#negative index [-3,-2,-1]

print(var_listname[2])

from loguru import logger

var_labour_name = ["suma","manish", "labour1", "labour2"]
logger.info(f"first element of list: {var_labour_name[0]}") #positive indexing

logger.info(f"first element of list: {var_labour_name[0]}")

# update list with single value use append
var_labour_name.append("ram") # only works for 1 value
print(f"appended value {var_labour_name}")

# update list with multiple value use extend
var_new_labour = ["rama","mama"]
var_labour_name.extend(var_new_labour)
print(f"extended value {var_labour_name}")

# add new values in starting of list using insert
var_new_labour = "dolu","molu"
var_labour_name.insert(0,var_new_labour)
print(f"inserted value {var_labour_name}")

#multidimensional list
var_labour_with_cost = [["suma",1000],["manish",1200],["rama",500],["mama",400]]

#access using index
logger.info(f"first labour name is {var_labour_with_cost[0][0]} and wage is {var_labour_with_cost[0][1]}")

