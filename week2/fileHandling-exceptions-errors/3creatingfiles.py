# file created and closed and data added 
# with open ('names.txt' ,'w') as file : 
    # file.write("hello file ")



with open('names.py' ,'w') as f:
    f.writelines(["\n usman \n" 'waqas \n'])
    

with open ('names.py' ,'r') as f:
   data= f.readlines()
   for d in data :
    print(d)

