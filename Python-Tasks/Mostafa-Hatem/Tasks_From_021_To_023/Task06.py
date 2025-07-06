friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


del friends[0:2]
print(friends)

friends.remove("Salem")
print(friends)


# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]