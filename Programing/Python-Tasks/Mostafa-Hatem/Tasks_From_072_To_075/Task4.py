

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")


filtered = [skill for skill in skills if not isinstance(skill, int)]

reversed_filtered = filtered[::-1]

for i, skill in enumerate(reversed_filtered):
    print(f'"{50 + i} - {skill}"')


print("#" * 10)

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = 50
for skill in reversed(skills):
    if not isinstance(skill, int):
        print(f'"{index} - {skill}"')
        index += 1

        