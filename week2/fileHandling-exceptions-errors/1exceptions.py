from logging import exception


def div_by_zero(x,y):
    return (x/y)

# print(div_by_zero(40,0)) # itll give error  division by zero
try:
  print(div_by_zero(40,0))
except Exception as e:
    print(f'some thing went wrong {e}')


# problem1 
# Starter code
items = [1,2,3,4,5]
try:
  item = items[6]
  print(item)
except: 
    print("item canot be found in list  ")


print("more later .......... aug/1/2022 ")
 hola