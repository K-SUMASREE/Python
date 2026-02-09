print("Programming is easy")

#Variables
VarLength = 100
print(VarLength)
print(id(VarLength))

#if two variables are assigned with same value then id will be same
# example same address in RAM
VarLength = 100
VarBreadth = 100
print(VarLength, VarBreadth)
print(id(VarLength),id(VarBreadth))

# example diff address in RAM
VarLength = 100
VarBreadth = 200
print(VarLength, VarBreadth)
print(id(VarLength),id(VarBreadth))

# Variable naming convension in python
"""
1. a-z, A-Z, _
2. number can be used but not at first
3. case sensitive ex: length,LENGTH, Length (all are diff)
4. keywords cant be used
5. use words seperated by underscore or camel casing
ex: var_name, VarName
* Underscore(_) most prefered
"""

#DATA TYPES
"""
Integer - positive and negative num ex: 100, -100, 0
Float - decimal ex: 10.100
String - "Suma"
Boolean - True, False
"""

length_of_land = 100
bricks_cost_per_price = 10.5
labour_name1 = "suma" 
# if string is not given inside quotes then it will be considered as variable
is_home = True
print(length_of_land,bricks_cost_per_price,labour_name1,is_home)
# print type of variable or value
print(type(length_of_land),type(bricks_cost_per_price),type(labour_name1),type(is_home))