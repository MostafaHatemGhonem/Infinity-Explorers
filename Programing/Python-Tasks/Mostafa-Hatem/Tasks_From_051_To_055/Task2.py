
for num in range(21):
    if num == 6 or num == 8 or num == 12:
        continue
    else:
        print(str(num).zfill(3))
print("All Numbers Printed")