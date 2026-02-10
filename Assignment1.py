'''
Q1. Define a variable of all the labours and print the name of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
    labour variable should be something like this 1st_labour, 2nd_labour and so on.

'''
var_1st_labour = "Mahesh"
var_2nd_labour = "Mithilesh"
var_3rd_labour = "Ramesh"
var_4th_labour = "Sumesh"
print(var_1st_labour,var_2nd_labour,var_3rd_labour,var_4th_labour)



'''
Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
    labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
    2nd_labour_wage and so on.
    You are bound to use string formatting
'''
Var_1st_labour_wage = 500
Var_2nd_labour_wage = 400
Var_3rd_labour_wage = 400
Var_4th_labour_wage = 300
print(f"name of 1st labour is {var_1st_labour} wage is {Var_1st_labour_wage} \nname of 2nd labour is {var_2nd_labour} wage is {Var_2nd_labour_wage} \nname of 3rd labour is {var_3rd_labour} wage is {Var_3rd_labour_wage} \nname of 4th labour is {var_4th_labour} wage is {Var_4th_labour_wage}")

'''
Q3. I want to print this paragraph and its line number from which this paragraph is printing
    """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
    I have to print this paragraph as it is given here."""
    Condition:- 
    You can't use triple quote.
    Triple quote at starting is also a part of paragraph.
'''
from loguru import logger
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger.info('''
""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
    I have to print this paragraph as it is given here."""

''')


'''
Q4. When do we get NameError?

'''
#python name error occurs when interpreter encounters an identifier (name) that has not been defined or is not accessible with current scope



'''
Q5. Python is a high level language. What does that mean by high level?
'''
# ans: high level language means human understandable code which is not byte or binary code
'''
Q6. What is compiled and Inetrpreted language, list a few?
'''
# compiled means whole code is executed at once like c++ interpreted means each line is run at once like python
# interpreted is slow
'''
Q7. Get all varibales address from RAM and you find if something is similar?
'''
print(id(Var_1st_labour_wage),id(Var_2nd_labour_wage),id(Var_3rd_labour_wage),id(Var_4th_labour_wage))