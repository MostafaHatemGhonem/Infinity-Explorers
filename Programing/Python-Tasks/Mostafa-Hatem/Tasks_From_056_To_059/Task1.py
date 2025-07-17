

def calculate(num1 , num2, op = 'subtract'):
    op = op.strip().lower()
    if op == "subtract" or op == "s":
        return num1 + num2
    elif op == "multiply" or op == "m":
        return num1 * num2
    elif op == "add" or op == "a":
        return num1 + num2
    else:
        return "Thanks."



# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200