subjects={"Math": "90", 
"Science":"80", 
"Language":" 70"
} 
def get_scores(*name,**subjects): 
    if subjects and name: 
        print(f"Hello {name[0]} this is your school table:")
        for subject,score in subjects.items():
            print(f"-{subject.capitalize()}==>{score}") 
    elif name: 
            print(f"Hello {name[0]} You have no scores to show")       
    else: 
        for subject,score in subjects.items():
            print(f"-{subject.capitalize()}==>{score}")           
get_scores("Osama", **subjects)
print("-"*30)
get_scores("Osama")
print("-"*30)
get_scores(**subjects)    
    