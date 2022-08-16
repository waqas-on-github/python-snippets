import sys 
import sys

# cammand line arguments with sys module 
if(len(sys.argv)!=2):
   print("too few arguments")
   sys.exit()
else:
 print('hello mr ' ,sys.argv[1])
