from csv import Dialect

# way no 1 
file =open("python-snippets/Topics_to_learn.txt" ,mode='r')
print(file.readline())
file.close()


# the second and easy way 
print("................the second and easy way ...........")
 
with open('python-snippets/week1/1hello.py' ,mode='r') as f  :
    print(f.readline())
# automatically closed 

