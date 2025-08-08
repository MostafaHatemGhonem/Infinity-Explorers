def remove_char(name): 
    cleaned_name=name[1:-1]
    return cleaned_name
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list=map(remove_char,friends_map) 
for name in cleaned_list:
    print(name)     
print("*"*30)    
cleaned_list=map(lambda name:name[1:-1],friends_map) 
for name in cleaned_list: 
    print(name) 