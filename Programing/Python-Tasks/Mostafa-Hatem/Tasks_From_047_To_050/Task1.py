# Input
num = int(input("Enter Your Number: "))

if num > 0:
    for i in range(num - 1, 0, -1):
        print(i)
        if i == 6:
            continue
    print(f"{i} Number Printed Successfully.")
else:
    print(f"Number {num} Is Not Larger Than 0")
