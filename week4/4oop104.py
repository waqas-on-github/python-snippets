# Topics 
# 1 CLASS METHODS 
# 2 STATIC METHODS 
# 3
# 4
import csv

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

    @classmethod
    def csv_to_instance(cls):

      with open('coursera-python/python-snippets-main/week4/data.csv','r') as f:  
        data=csv.DictReader(f)
        items =list(data)

        for i in items:
            Item(
                name=str(i.get("name")),
                quantity=int(i.get("quantity")),
                price=int(i.get("price"))
            )
            


Item.csv_to_instance()

car=Item("city" ,100,100000)

print(Item.all)
# We can read all instances data by just loopin on item.all
print(car.calculate_price())

