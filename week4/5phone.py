

class Item:

    all=[]
    pay_rate = 0.8 # class attribute   
    # constructor  make instances 
    def __init__(self,name:str ,price:float  ,quantity=0):  # --> REF=01  
        # validations 
        assert price>=0, print(f'price {price} is not greater then and equal 1')
        assert quantity >=0,print(f'quantity  {quantity} is not greater then zero ')
        # attributes 
        self.name =name
        self.price=price
        self.quantity=quantity
        # tracking instances 
        Item.all.append(self)


    # mehtods 
    def calculate_price(self):
        return(f' {self.name } total price is :{self.price*self.quantity}')
    
    def apply_discount(self):
        self.price=self.price * self.pay_rate
        return (self.price)
    
    def __repr__(self):
        return(f" {self.name} , {self.price} {self.quantity}")

#crate object and intanciate them with item class 
leptop=Item("mackbook pro", 1000 ,30)
clock = Item('clock x ' ,10,200)
mouse=Item('appel mouse ' ,2,90)
book =Item('dsa with python' ,1 ,100)
  
# phone class borowing methods from Item class  "INHERTANCE"
class Phone(Item):
    # construcrtor 
    def __init__(self, name: str, price: float, quantity=0 ,Broken_phone=0):
        super().__init__(name, price, quantity)
         
        self.Broken_phone=Broken_phone
        assert Broken_phone>=0,print(f"{Broken_phone} is not greater then zero") 
    #  methods 


# print(Item.__dict__)
# print(Phone.__dict__)

phone1=Phone('samsung' ,22.5,20,1)
print(phone1.Broken_phone)
print(phone1.calculate_price())   # Borrowed from item class 
print(phone1.apply_discount())     #Borrowed from item class 

     
print(Item.all)
print(Phone.all)




























