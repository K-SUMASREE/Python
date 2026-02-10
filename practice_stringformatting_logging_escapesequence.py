# refer docs.python.org or chatgpt 
#use control + forward slash to comment a line
# use """ or ''' to comment multiple lines

length_of_land = 100
bricks_cost_per_price = 10.5
labour_name1 = "suma" 
# if string is not given inside quotes then it will be considered as variable
is_home = True

# print is used to display output
print(length_of_land) #gives only 100 which is not clear what output it is
print("length_of_land",length_of_land) 
print('length_of_land',length_of_land) 

# print multiple outputs using one print statement
print('length_of_land:',length_of_land, 'bricks_cost_per_price:',bricks_cost_per_price)
#print using f-string
print(f"length_of_land:{length_of_land}, bricks_cost_per_price:{bricks_cost_per_price}")

# I want output as my home is 4 BHK and in next line length of total land is 100
#use escape sequence to print new line in single print (\n)
# string formatting print(f"")
print(f"my home is 4 BHK \n length of total land is {length_of_land}")

# we can also do this without escape sequence using '''

print('''my home is 4 BHK
length of total land is {length_of_land}''')

# print 4bhk in double quote

print('my home is "4 BHK"')

# use double quote at start as well 
# for this we have escape sequence \ to skip one character

print("my home is \"4bhk\"") #skips "

#escape sequence for spacing \t-4 spacing

print("a\tb")

# .format method
print("bricks_cost {} length_of_land {} labour is {}".format(bricks_cost_per_price,length_of_land,labour_name1))

# logging
# %(asctime)s for time, %[%(filename)s:%(lineno)d] to know the line num in code

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("Something went wrong")
logging.info(f"length_of_land:{length_of_land}, bricks_cost_per_price:{bricks_cost_per_price}")


#use pip install loguru in terminal to install library
# logger gives more clean look
from loguru import logger
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Program started")
logging.info(f"length_of_land:{length_of_land}, bricks_cost_per_price:{bricks_cost_per_price}")
logger.info(f"length_of_land:{length_of_land}, bricks_cost_per_price:{bricks_cost_per_price}")