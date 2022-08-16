
class Book:
#   constructor
    def __init__(self ,catgory:str):
          self.__catgory=catgory


    @property
    def catgory(self):
           return self.__catgory

    @catgory.setter 
    def catgory(self,value):
        if(len(value)>7):
          self.__catgory = value


dsa=Book("compu")
print(dsa.catgory)
dsa.catgory="hompu"

      

