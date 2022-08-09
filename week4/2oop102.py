# Topics 
# 1 class attribute 
# 2
# 3
# 4
# 5



class Item:
    pay_rate = 0.8 # class attribute   
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

    def apply_discount(self):
        self.price=self.price * self.pay_rate
        return (self.price)
#   crate object and intanciate them with item class 

phone =Item("iphone x " ,1000,10)
print(phone.calculate_price())


leptop=Item("mackbook pro", 1000 ,30)
print(leptop.calculate_price())

print(Item.pay_rate)
print(phone.pay_rate) # if attr not fount at instance level itll fint on class level 
print(leptop.pay_rate)

print(Item.__dict__)   # will show all attributes regarding to that class or instance 
print(phone.__dict__)


# applyin specfic discount to desired item 

phone.pay_rate=0.7
phone.apply_discount()
print(phone.price)

print(phone.price)
phone.apply_discount()
print(phone.price)
print(phone.calculate_price())