def get_names(name): 
    new_names=name.endswith("m") 
    return new_names
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names=filter(get_names,friends_filter) 
for name in names: 
    print(name) 
print("*"*30)
names=filter(lambda name:name.endswith("m"),friends_filter) 
for name in names: 
    print(name) 
