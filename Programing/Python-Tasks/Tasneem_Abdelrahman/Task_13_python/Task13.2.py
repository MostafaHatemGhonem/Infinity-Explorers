def get_scores(*name,**subjects): 
    if subjects and name:
        print(f"Hello {name[0]} this your school table:") 
        for subject,score in subjects.items():
            print(f"-{subject.capitalize()}==>{score}") 
    elif name:
             print(f"Hello {name[0]} You have no scores to show") 
    else: 
        for subject,score in subjects.items():
            print(f"-{subject.capitalize()}==>{score}")  
get_scores("Osama", Math=90, Science=80, Language=70)
print ("*"*30)
get_scores("Mahmoud", Logic=70, Problems=60)
print ("*"*30)
get_scores(Logic=70,problems="60") 
print ("*"*30)
get_scores("Ahmed")  
    
    