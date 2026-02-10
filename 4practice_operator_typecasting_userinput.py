'''
1. what are operators?
2.how bodmas rule works?
3.what is floor and cell in python?
4.what is modulo operator?
5.types of type casting?
6.how can i take input from users?
'''
# ===============================
# PYTHON OPERATORS - NOTES
# ===============================

# 1. Arithmetic Operators
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division (float result)
# //  Floor division
# %   Modulus (remainder)
# **  Power

# Examples:
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1
# 2 ** 3 = 8


# 2. Comparison Operators
# ==  Equal
# !=  Not equal
# >   Greater than
# <   Less than
# >=  Greater than or equal
# <=  Less than or equal

# Example:
# a = 10
# b = 5
# a > b   -> True
# a == b  -> False


# 3. Assignment Operators
# =    Assign
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# //=  Floor divide and assign
# %=   Modulus and assign
# **=  Power and assign

# Example:
# x = 10
# x += 5   -> 15
# x -= 3   -> 12


# 4. Logical Operators
# and   True if both are True
# or    True if any one is True
# not   Reverse the result

# Example:
# a = True
# b = False
# a and b -> False
# a or b  -> True
# not a   -> False


# 5. Bitwise Operators
# &   AND
# |   OR
# ^   XOR
# ~   NOT
# <<  Left shift
# >>  Right shift

# Example:
# 5 & 3 -> 1
# 5 | 3 -> 7


# 6. Membership Operators
# in       True if value exists
# not in   True if value does not exist

# Example:
# 'a' in 'cat'      -> True
# 'z' not in 'cat' -> True


# 7. Identity Operators
# is       True if both refer to same object
# is not   True if not same object

# Example:
# a = [1, 2]
# b = a
# c = [1, 2]
# a is b  -> True
# a is c  -> False

from loguru import logger
import math 

var_length_of_land = 100
var_breadth_of_land = 100
var_bricks_cost_per_price = 10.5
var_labour_name1 = "suma" 
var_labour_name2 = "manish"
var_is_home = True

#calculate the total area of land

var_total_area_of_land = var_length_of_land * var_breadth_of_land
logger.info(f"Total area of land is {var_total_area_of_land} sq ft")

#perimeter 
# BODMAS
var_perimeter_of_land = 2 * (var_length_of_land + var_breadth_of_land)
logger.info(f"perimeter of land is {var_perimeter_of_land} ft")

# modulus operator gives reminder
var_modulo = 15%2
print (f"modulo is {var_modulo}") #reminder 1, Armstrong number

# Floor division (if output is 2.2 it gives 2)
# Ceiling division (if output is 2.2 it gives 3)
# import math library to do these
var_floor=math.floor(15/7)
var_ceil=math.ceil(15/7)
print(f"floor value is {var_floor}") #output 2
print(f"ceil value is {var_ceil}") #output 3

a= "25"
b= "35"
print(a+b) # considered as string and concatenates the variables

'''
this gives concatenation error because data type is different
a= "25"
b= 35
print(a+b)
'''

#type casting means converting the data type

a= "25"
b= 35
var_typecasting_a_integer=int(a)+b
var_typecasting_b_string = a+str(b)
print(f"typecasted integer output is {var_typecasting_a_integer}, typecasted string output is {var_typecasting_b_string}")

#types of type casting
# 1. explicit -> developer
# 2. implicit -> python does by its own

#example 
a = 1.5
b = 7
print(a+b) #integer cant be sum with float so python converted b = 7 to float 7.0 and gave output in float

# take input from user

var_length_of_land = float(input("please enter the length of your land"))
var_breadth_of_land = input("please enter the breadth of your land")
#logger.info(f"{type(var_length_of_land)}")
var_total_area_of_land = int(var_length_of_land * float(var_breadth_of_land))
logger.info(f"Total area of your land is : {var_total_area_of_land}")

#absolute abs gives output only in positive value

var_length_of_land = float(input("please enter the length of your land"))
var_breadth_of_land = input("please enter the breadth of your land")
#logger.info(f"{type(var_length_of_land)}")
var_total_area_of_land = abs(var_length_of_land * float(var_breadth_of_land))
logger.info(f"Total area of your land is : {var_total_area_of_land}")

#typecasting 