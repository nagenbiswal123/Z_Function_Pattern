#Below a and b are the Global variables 
#Always write a variable name in proper syntax/proper name, otherwise Interviewer will think you don't have the real Experience.
#Ruleno1: Always declare a variable in small case
#If you variable name in 2 part like it below, EC2_Instance_Name

a=9
b=3

def addition():
    c=23 #Local scope Variable
    print(a + b + c)

def sub():
    print(a - b)

addition()
sub()
