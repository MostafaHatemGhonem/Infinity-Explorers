
my_friends = []            
max_friends = 4            

while len(my_friends) < max_friends:
    name = input("Enter Your Name: ").strip()   

    if name.isupper():
        print(f"Invalid Name: {name}")
    elif name.islower():
        name = name.capitalize()   
        my_friends.append(name)
        print(f"Friend {name} Added => 1st Letter Become Capital:")
    elif name[0].isupper():
        my_friends.append(name)
        print(f"Friend Ahmed{name} Added")
    else:
        my_friends.append(name)
        print(f"Friend Ahmed{name} Added")

    remaining = max_friends - len(my_friends)
    if remaining > 0:
        print(f"You Can Add More {remaining} Friends")
    else:
        print("Done")

