

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  # Write Your Code Here
    my_data.append(data)
    print(my_data)

my_data = list(my_data)

final_string = "".join([str(item) for sublist in my_data for item in sublist])

print(final_string.capitalize()) # Elzero