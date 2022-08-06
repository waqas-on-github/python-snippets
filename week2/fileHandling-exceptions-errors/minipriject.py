import os

#  you can read ,create ,update ,delete  any file using this python cli application  


def read_file(path):  
    with open(path ,'r') as f:
        print(f.readlines())



def make_file(file_name,*kwargs):
    with open(f'{file_name}','w') as file :
        data =kwargs
        for d in data :
           file.writelines([d])


def update_file(path,*kwargs):
    with open(f'{path}','a') as file :
        data=kwargs
        for d in data :
           file.writelines([d])

print("read_file --> rdf \ncrate_file --> to crf \nupdating_file --> upd\ndelete_file --> df \n ")
command=input(":_")


if(command=="crf"):
    f=input('fileName  : ')
    data=input("enter data")
    make_file(f,data )

elif(command=='upd'):
    path=input("file path :")
    data=input("enter data")
    update_file(path,data)

elif (command=='rdf'):
    path=input('path')
    read_file(path)

elif (command=='df'):
    path=input('path')
    os.remove(path)
else:
    print("enter right command ...")
