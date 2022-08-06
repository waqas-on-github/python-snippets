
# NOTE sets are unorderd and uniuqe 
seta ={1,2,3,4,5,3}
print(type(seta))
print(len(seta))
print(seta)
# adding a values 
seta.add(6)
seta.add(77)
print('..............6,77 added.......................')
print(seta)

# removing values 
print('.........77 removed ................')
seta.remove(77)
print(seta)


# math with sets 

setb={2,4,6,7,8,9}
print("....................union of seta and setb.............. ")
print(seta.union(setb))
print("....................intersection of seta and setb.............. ")
print(seta.intersection(setb))
print("....................diffrence of seta and setb.............. ")
print(seta.difference(setb))
print("....................semmetrical diff  of seta and setb.............. ")
print(seta.symmetric_difference(setb))

print('..................itrating of sets ')
for i in seta:
    print(i)


