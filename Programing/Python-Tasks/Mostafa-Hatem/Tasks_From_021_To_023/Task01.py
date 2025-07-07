


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(f"Method One: {friends[0]}")
print(f"Method Two: {friends[friends.__len__() - friends.__len__()*2 ]}")
print(f"Method One: {friends[-5]}")
print(f"Method Two: {friends[0:1]}")
print(f"Method One: {friends[4]}")
print(f"Method Two: {friends[-1]}")

print(friends.__len__())

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two