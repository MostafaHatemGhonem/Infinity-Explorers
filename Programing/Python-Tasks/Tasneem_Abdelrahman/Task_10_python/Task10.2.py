friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i=0
ignored=0
while i < len(friends): 
    if friends[i][0].islower(): 
        ignored+=1
    else: 
        print(friends[i])     
    i+=1
print(f"friends printed and ignored names={ignored}") 
  