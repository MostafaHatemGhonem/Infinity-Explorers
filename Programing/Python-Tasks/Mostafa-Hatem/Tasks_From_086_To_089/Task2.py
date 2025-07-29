

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  # Write Your Code Here
#     my_data.append((item1, item2, item3))
    my_data.append((item1, item2, item3))

final_string = my_data.__str__().replace("'", "").replace(",", "").replace("(", "").replace(")", "")

print(final_string)