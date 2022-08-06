# example of paladrom =abba -->  read form start or end word will be same 






def isPaladrom(str):
     high=0
     low =len(str) -1     
     for s in str:
        print(s)
        print(str[high])
        print(str[low])
        if(str[high]!= str[low]):
            return (False)
         
        return(True)

print(isPaladrom('ababcababa'))





