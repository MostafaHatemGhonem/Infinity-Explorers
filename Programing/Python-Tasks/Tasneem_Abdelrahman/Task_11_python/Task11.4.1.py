students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
for name in students:
    count=0
    print("*"*30)
    print(f"student name ==> {name}")
    print("*"*30)
    for subject in students[name]: 
        for degree in students[name][subject]: 
                if degree=='A': 
                   print(f"-{subject} ==> 100 points")
                   count+=100
                elif degree=='B': 
                   print(f"-{subject} ==> 80 points") 
                   count+=80
                elif degree=='C': 
                   print(f"-{subject} ==> 40 points") 
                   count+=40
                else: 
                   print(f"-{subject}==> 20 points")   
                   count+=20
    print(f"Total points for {name} is {count}") 