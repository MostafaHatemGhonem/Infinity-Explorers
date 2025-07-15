# Input
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

grades_points = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

for name in students:
    print("------------------------------")
    print(f"-- Student Name => {name}")

    student_subjects = students[name]
    for subject in student_subjects:
        print(f"- {subject} => {student_subjects[subject]}")


for student_name, subjects in students.items():
    print("------------------------------")
    print(f"-- Student Name => {student_name}")
    
    total = 0
    for subject_name, grade in subjects.items():
        points = grades_points[grade]
        print(f"- {subject_name} => {points} Points")
        total += points
    
    print(f"Total Points For {student_name} Is {total}")


# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"