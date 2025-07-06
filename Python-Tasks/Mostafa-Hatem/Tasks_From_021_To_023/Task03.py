

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

a = friends.index("Ahmed")

print(friends[a : a + 3])

after_end = friends.index("Ali")

print(friends[after_end : after_end + 2])


# if Q mean acisss on elment not this

print(friends[1:4])  
print(friends[-2:]) 

# ###########################################

#try

#if You Want Name
friends.append("Mostafa")
friends.insert(0, "Hatem")

print(friends)

a = friends.index("Ahmed")

print(friends[a : a + 3])

after_end = friends.index("Ali")

print(friends[after_end : after_end + 2])


#if You Want positon

print(friends[1:4])  
print(friends[-2:]) 

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"