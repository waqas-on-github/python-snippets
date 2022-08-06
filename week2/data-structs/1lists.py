

resource_to_datastruct="https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/zVPJ6v2bRB-Tyer9m1Qf5A_33700a0849b040bf8f8afefe2a38ebe1_BED_C2M2L1_item04-img01.png?expiry=1659225600000&hmac=DIgNGzzOZcN_zoLtM1znKe1ajXjZCFqBsIRoc5TnuUI"
# python lists
friends =['waqas' ,'usman' , "imran"]
# looping on lists 
for item in friends: 
    print(item)

# accesing data in lists 

print("..................................accesing data in lists.............................")
print(friends[0])
print(friends[0:2])
print(friends[-1])
print(friends[:])

# adding removing data in lists 
print("................................adding removing data in lists.....................................")
friends.append("mama")
print(friends) # get a new friend 
friends.pop()
print(friends) #a friend leave a group 
friends.pop()
print(friends) #a friend leave a group 
friends.pop()
print(friends) # im still here 

# Example from google education 
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
