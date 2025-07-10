nums = {1, 2, 3}
letters = {"A", "B", "C"}
nums.update(letters)
print(nums)
print(nums|letters)
nums.union(letters)
print(nums)





# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}