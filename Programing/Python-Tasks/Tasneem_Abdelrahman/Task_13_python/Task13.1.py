def get_score (**subjects): 
    for subject,score in subjects.items(): 
        print(f"-{subject.capitalize()} ==>{score}") 
get_score(Maths="90",Science="80",language="70", logic="60",problems="50")     
    