

def show_skills(name, *skills):
    print(f"Hello {name}", end=" ")

    if skills:
        print("Your Skills Is")
        for skill in skills:
            print(f"- {skill}")
    else:
        print("You Have No Skills To Show")


# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

# Input
show_skills("Ahmed")
