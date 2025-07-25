myfriends=[]
maxnames=4
while maxnames<=4 and maxnames>0:
    name=input("please enter the name: ")
    if name==name.upper(): 
        print("invalid name") 
    elif name[0].isupper():
        print(f"friend {name} Added!") 
        maxnames-=1
        print(f"names left in list is {maxnames}"if maxnames>0 else"list is filled") 
    else:
        name=name.capitalize().strip() 
        print(f"friend {name} Added => 1st letter become capital") 
        maxnames-=1
        print(f"names left in list is {maxnames}"if maxnames>0 else"list is filled") 
    


    