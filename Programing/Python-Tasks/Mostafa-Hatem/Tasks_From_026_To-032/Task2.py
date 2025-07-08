nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
print(nums.union(letters).union({1, 2, 3}))
# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}