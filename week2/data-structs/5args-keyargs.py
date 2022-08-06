# simple funcation 
from cgi import print_arguments
from functools import total_ordering


def add(a,b,c):
    return(a+b+c)


print(add(2,3,5))


# function with args 

def addall(*args):
    print(type(args))
    sum=0
    for x in args:
        sum+=x
    
    return sum 
 
print(addall(2,3,456,45,67,5))

def sumof(**kwargs):
    sum=0
    for k,v in kwargs.items():
        sum+=v
    return sum


print(sumof(k=1, j=2,l=3))
