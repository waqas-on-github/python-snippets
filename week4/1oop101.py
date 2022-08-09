# 1 classes 
# 2 class constructor 
# 3 class methods 
# 4 class instances 

# .............OOP............. 
# The basic idea of OOP is to divide a sophisticated program into a
#  number of objects that talk to each other.

#  NOTE REF01 --> you can mention data type in two ways 1: optional parameter or mention data type 
# TPICS COVERD 


class Item:
    # constructor 
    def __init__(self,name:str ,price:float  ,quantity=0):  # --> REF=01  
        self.name =name
        self.price=price
        self.quantity=quantity
        
        assert price>=0, print(f'price {price} is not greater then and equal 1')
        assert quantity >=0,print(f'quantity  {quantity} is not greater then zero ')

    # mehtods 
    def calculate_price(self):
        return(f' {self.name } total price is :{self.price*self.quantity}')


#   crate object and intanciate them with item class 

phone =Item("iphone x " ,10,999)
print(phone.calculate_price())


leptop=Item("mackbook pro", 10 ,9999.99)
print(leptop.calculate_price())

