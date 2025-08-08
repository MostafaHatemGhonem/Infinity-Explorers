skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
reversedskills=reversed(skills) 
myskillswithcounter=enumerate(reversedskills,50)
for counter,skill in myskillswithcounter: 
    if type(skill)==str: 
        print(f"{counter}-{skill}") 
        
print("*"*30)
        
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript") 
count=49
for skill in reversed(skills): 
    if type(skill)==str: 
         count+=1
         print(f"{count}-{skill}")
    else:
        count+=1   