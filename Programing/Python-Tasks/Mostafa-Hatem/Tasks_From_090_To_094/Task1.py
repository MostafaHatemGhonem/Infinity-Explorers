
NUM = input("Add Your Number ")

if len(NUM) > 1:
    raise IndexError("Only One Character Allowed")

if not NUM.isdigit():
    raise TypeError("Only Integer Allowed")

NUM = int(NUM)

if NUM == 0:
    raise ValueError("Number Must Be Larger Than 0")

print("#"* 15 )
print(f"Your Number is: {NUM}" )
print("#"* 15 )
