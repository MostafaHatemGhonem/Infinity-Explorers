def show_skills(name,*skills): 
    if skills: 
        print(f"Hello {name.capitalize().strip()} your skills are:") 
        for skill in skills: 
            print(f"-{skill}") 
    else:
         print(f"Hello {name.capitalize().strip()} you have no skills to show")   
show_skills("tasneem","Python ","Html","CSS","Js") 
show_skills("Osama") 
