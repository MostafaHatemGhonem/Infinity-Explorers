

def remove_chars(name) -> str:
    return name[1:-1]




friends_map =  ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Output
print("#" * 10)

for friend in friends_map:
    print(remove_chars(friend))


print("#" * 10)

cleaned_list = list(map(remove_chars, friends_map))


for friend in cleaned_list:    print(friend)
print("#" * 10)


print(list(map(lambda person: person[1:-1], friends_map)))