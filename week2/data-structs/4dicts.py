
# NOTE  keys cant be similar/duplicated 


simple_dict= {1:'coffe' ,2:'tea'  ,3: 'juce'} # declaring a dict 

# 2 accesing items from dict 
print(".................accesing items from dict....................................")
print(simple_dict[1])

# 2nd way 
print(simple_dict.get(2))

# 3 updating /changing items 
print(' ....................... updating /changing items from dict ....................')
simple_dict[1]= "black-tea"
print(simple_dict)
# Removing elements from Dictionary
print('..........................Removing elements from Dictionary.................................')
del simple_dict[3]
simple_dict.pop(2)
print(simple_dict)

# adding items in dict 
print('.................. adding items in dict.........................')
simple_dict[3]='juice'
print(simple_dict)
# Iteration/enumerate on dict 
print('......................Iteration/enumerate on dict .................. ')
for items in simple_dict:
    print(items)

print(".......................... enumarating on dicts .........................")

for key,val in simple_dict.items():
    print(f' key is {str(key)} and value is {val} ')




