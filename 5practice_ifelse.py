'''
where do we use this in real time
1.to check if output is expected or not
2.check whether variable or list is not empty
3.check if dataframe is not empty
4.backdated job run
5.to raise some error
'''
# python que: check the number of BHK home and based on length and breadth check if that is possible or not and provide answer to customer

# if runs based on true or false
# conditional statement can be given in if and else not in elif

from loguru import logger
import math 

var_length_of_land = 100
var_breadth_of_land = 100
var_bricks_cost_per_price = 10.5
var_labour_name1 = "suma" 
var_labour_name2 = "manish"
var_is_home = True

var_length_of_land = int(input("Enter the length of land: "))
if (var_length_of_land < 100):
    logger.info(f"Your land length is not sufficient to build a 4BHK")
    if (var_length_of_land >= 80):
        logger.info(f"Your land length is sufficient to build 3BHK")
    if (var_length_of_land >= 60):
        logger.info(f"Your land length is sufficient to build 2BHK")
    if (var_length_of_land >= 25):
        logger.info(f"Your land length is sufficient to build 1BHK")
    else:
        logger.info(f"Your land length is not sufficient to build a house")
elif(var_length_of_land >= 500):
    logger.info(f"You can build more than 2 buildings")
else:
    logger.info(f"Share more details with us")

# how will you find out if given number is even or odd
# first write a sequence of flow then implement it
var_number = int(input("please enter a number: "))
var_result = var_number%2
if (var_result == 0):
    logger.info(f"The number you have provided is even")
else:
    logger.info(f"The number you have provided is odd")
