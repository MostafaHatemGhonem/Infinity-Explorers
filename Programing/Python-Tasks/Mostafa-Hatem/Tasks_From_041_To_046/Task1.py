# Inputs

num1 = int(input("Enter The First Number: "))
operation = input("Enter Operation: ")
num2 = int(input("Enter The Second Number: "))



if operation == "+":  
    print(f"{num1} {operation} {num2} = {num1 + num2}")
elif operation == "-": 
    print(f"{num1} {operation} {num2} = {num1 - num2}")
elif operation == "/":
    print(f"{num1} {operation} {num2} = {num1 / num2}")
elif operation == "*":
    print(f"{num1} {operation} {num2} = {num1 * num2}")
elif operation == "**":
    print(f"{num1} {operation} {num2} = {num1 ** num2}")
elif operation == "%":
    print(f"{num1} {operation} {num2} = {num1 % num2}")
else:
    print("Invalid operation")



# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800 