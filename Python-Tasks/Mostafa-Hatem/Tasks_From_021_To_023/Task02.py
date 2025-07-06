

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])


for i in friends:
    if friends.index(i) % 2 == 0:
        print(i, end=", ")

print()

for i in friends:
    if friends.index(i) % 2 != 0:
        print(i, end=", ")


# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"