for number in range(1,21): 
    if number==6 or number==8 or number==12:
        continue 
    print(str(number).zfill(2)) 
print("All numbers are printed") 