


friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

ignored_count = 0

for name in friends:
    if name[0].isupper():
        print(name)
    else:
        ignored_count += 1

print(f"Friends Printed And Ignored Names Count Is {ignored_count}")
