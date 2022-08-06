# implicit type casting happen by python engine automaticly 
from email.utils import parsedate_to_datetime


num1=22
num2=66.66
print(f'type of num1{type(num1)} and type of num 2 {type(num2)}')
result=num1+num2
print(result)
print(type(result))
# explicit type casting  
n1='11'
n2=22
print(f'type of num1{type(n1)} and type of num 2 {type(n2)}')
print(int(n1)*n2) # itll through error  or unexpected result 


num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
# print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum)   #Traceback (most recent call last):File "<string>", 
# HOW TO FIX 
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))
# What this means is, I cannot concatenate a string and a float like that. In other words, although Python's implicit type conversion works when I use the + operator on strings and integers, it does not work on strings and floats.




  

