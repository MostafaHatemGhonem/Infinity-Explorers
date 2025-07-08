

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

my_list = list(set(my_list))
my_list.sort()
print(my_list)
print(type(my_list))
print(*my_list, sep=', ')

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
