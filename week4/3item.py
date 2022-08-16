# 1 __repr__  method 
# 2 tracking instances 

# .............OOP............. 
# The basic idea of OOP is to divide a sophisticated program into a
#  number of objects that talk to each other.

#  NOTE REF01 --> you can mention data type in two ways 1: optional parameter or mention data type 
# TPICS COVERD 

class Item:

    # class attribute  
    all=[]

    # constructor 
    def __init__(self,name:str ,quantity:int,price:float):  # --> REF=01  
        # run validation to the recived arguments
        assert price>=0, print(f'price {price} is not greater then and equal 1')
        assert quantity >=0,print(f'quantity  {quantity} is not greater then zero ')
        # assign to self object
        self.name =name
        self.price=price
        self.quantity=quantity
        #  action to execute 
        Item.all.append(self)

    # mehtods 
    def calculate_price(self):
       return(f' {self.name } total price is :{self.price*self.quantity}')

    def __repr__(self):
        return(f" {self.name} , {self.price} {self.quantity}")
    
#   crate object and intanciate them with item class 

phone =Item("iphone x " ,10,999)
leptop=Item("mackbook pro", 10 ,9999.99)
clock = Item('clock x ' ,10,200)
mouse=Item('appel mouse ' ,2,90)
book =Item('dsa with python' ,1 ,100)

print(Item.all)
# We can read all instances data by just loopin on item.all
for instance in Item.all:
    print(instance.name)




