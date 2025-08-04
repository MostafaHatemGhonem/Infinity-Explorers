my_nums = [15, 81, 5, 17, 20, 21, 13]
sorted_nums=sorted(my_nums,reverse=True) 
count=0
for number in sorted_nums: 
    if number%5==0:
        count+=1
        print(f"{count}==>{number}")
print("All numbers are printed")         
        