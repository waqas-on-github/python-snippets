# for loop
for i in range(10):
    print(i) 
   
# looping of strings 
for x in "banana":
    print(x)

# loopin on array  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# looping with conditionals
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)   

# ...............Break................
# The code works as intended but you may notice one flaw. 
# If you change the search term to something that is on the list like "Churros" and 
# run it again you will get the following output:
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')





# .................Continue.............
# Similar to break, continue can be used to control the iteration of the loop.
# The key difference is that it can allow you to skip over a section of the loop but
# then continue on with the rest. If you change your code to this, 
# you will notice the outcome will print everything except the Churros dessert.

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 



# ....................Pass..................
#The pass statement allows you to run through the loop in its entirety
#and effectively ignore that the if condition has been satisfied.
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 















#  .......... While loop ...
# On the other hand, a while loop is based upon a condition being true.
# Once the condition is no longer true the loop stops.
# The amount of times the while loop is executed is not known ahead of time as
# it is with the for loop. 

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0  # start of while loop 

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1   # end of while loop 


