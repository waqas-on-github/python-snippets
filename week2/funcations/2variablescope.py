# 1. Local scope
# Local scope refers to a variable declared inside a function. For example, in the code below,
# the variable total is only available to the code within the get_total function.
# Anything outside of this function will not have access to it.

# *NOTE.........WE CAN NOT ACCESSS VARIABLE FROM OUTSIDE.............. LOCAL SCOPE ............... 


def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))


# 2. Enclosing scope
# Enclosing scope refers to a function inside another function or what is commonly called a nested function. 

# *NOTE CHILD FUNCATION CAN ACCES DATA OF PARENT FUNCATION IN NESTED FUNCATIONS ..... ENCLOSED
# NOTE BUT PARENT CAN'T ACCES HIS CHILD DATA 
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2  # ---> CHILD FUNCATION CAN ACCES DATA OF PARENT
        print(double)

    double_it()
    #double variable will not be accessible
    # print(double) # ---> PARENT CAN'T ACCES HIS CHILD DATA

    return total
# 3. Global scope

# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere. 
special = 5
def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    # print(special)

    def double_it():
        #local variable
        double = total * 2
        print("globle variable value down"  )
        # print(special)
        print(double)

    double_it()
    return total


print("globle scope here !")
get_total(22,33)


# 4. Built-in scope
# Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth.  Functions with built-in scope can be accessed at any level.

