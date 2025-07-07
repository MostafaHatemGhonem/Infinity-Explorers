

friends = ("Osama", "Ahmed", "Sayed")


friends = ("Elzero",) + friends[1:]

print(friends)
print(type(friends))
print(friends.__len__())

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements