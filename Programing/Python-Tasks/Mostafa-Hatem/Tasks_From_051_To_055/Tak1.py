# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]

count = 0

for num in sorted(my_nums, reverse=True):
    if num % 5 == 0:
        count += 1
        print(f"\"{count} => {num}\"")
