
from os import name


def  get_names(name) : 
    if name.endswith("m"):
        return name
    else:
        return None
    

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]    

names = list(filter(get_names, friends_filter))

for name in names: 
    print(name)

print("#" * 10)

print(list(filter(lambda name: name.endswith("m"), friends_filter)))


# Output
"Wessam"
"Essam"